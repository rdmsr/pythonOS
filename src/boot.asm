section .bss
align 16
stack_bottom:
resb 8192
stack_top:

section .stivale2hdr
align 4
stivale_hdr:
    dq 0
    dq stack_top
    dq (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)
    dq 0
