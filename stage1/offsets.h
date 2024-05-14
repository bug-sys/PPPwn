#ifndef __OFFSETS_H__
#define __OFFSETS_H__
#if FIRMWARE == 1100 // FW 11.00
#define kdlsym_addr_Xfast_syscall 0xffffffff822001c0
#define kdlsym_addr_pppoe_softc_list 0xffffffff844e2578
#define kdlsym_addr_cc_cpu 0xffffffff844dde80
#define kdlsym_addr_callwheelsize 0xffffffff844dfe80
#define kdlsym_addr_nd6_llinfo_timer 0xffffffff82404e00
#define kdlsym_addr_Xill 0xffffffff824d2370
#define kdlsym_addr_setidt 0xffffffff8245bdb0
#define kdlsym_addr_kernel_map 0xffffffff843ff130
#define kdlsym_addr_kmem_alloc 0xffffffff82445e10
#define kdlsym_addr_kproc_create 0xffffffff822c3140
#define kdlsym_addr_kproc_exit 0xffffffff822C33b0
#define kdlsym_addr_ksock_create 0xffffffff824a9cc0
#define kdlsym_addr_ksock_close 0xffffffff824a9d30
#define kdlsym_addr_ksock_bind 0xffffffff824a9d40
#define kdlsym_addr_ksock_recv 0xffffffff824aa0a0
#define kdlsym_addr_uart_patch 0xffffffff8372cff8
#define kdlsym_addr_veri_patch 0xffffffff82823f64
#else
#error "Invalid firmware"
#endif
#define kdlsym(sym) (kaslr_offset + kdlsym_addr_##sym)
#endif
