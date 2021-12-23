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
    dq 24
    dq 0
