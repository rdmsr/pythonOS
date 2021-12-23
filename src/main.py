import stdint

VGA_GREEN: int = 0x2
VGA_WHITE: int = 0x7

# u16 is an unsigned 16-bit integer
# It was added by Snek to allow for better portability & systems programming

def print_to_vga(offset: int, character: u16, color: int):

    raw: u16 = (character) | color << 8

    # __builtin_write_mem is a special function that is used to write to memory
    # This is necessary because python does not have a direct way to write to memory
    # Params: addr, value, type
    __builtin_write_mem(0xb8000 + offset+1, raw, u16)


def print_str(string: str, size: int, color: int):
    for i in range(0, size):
        print_to_vga(i, string[i], color)

def _start():

    print_str("Hello World From Python!", 25, VGA_GREEN)

    asm ("1: jmp 1b")
