#!/usr/bin/env python
import os
import sys

files = ['src/main.py']
asm_files = ['src/boot.asm']
c_files = ['build/main.c']
output_files = ['build/main.c.o', 'build/boot.asm.o']

gcc_flags = [
    '-O2',
    '-Wall',
	'-I.',
	'-std=gnu11        ',
	'-ffreestanding    ',
	'-fno-stack-protector ',
	'-fno-pic          ',
	'-mabi=sysv        ',
	'-mno-80387        ',
	'-mno-mmx          ',
	'-mno-3dnow        ',
	'-mno-sse          ',
	'-mno-sse2         ',
	'-mno-red-zone     ',
	'-mcmodel=kernel   ',
	]

ld_flags = [
	'-Tsrc/linker.ld            ',
	'-nostdlib              ',
	'-zmax-page-size=0x1000 ',
	'-static'

]

def build_py():
	for i in files:
	    output = i.replace('src', 'build')
	    output = output.replace('.py', '.c')

	    d = "build"

	    if not os.path.exists(d):
	        os.makedirs(d)

	    os.system('thirdparty/snek/snek.py ' + i + ' ' + output)


def build_c():
	for output in c_files:
		command = "gcc "

		for i in gcc_flags:
			command += i + " "

		command += f" {output} -c -o {output + '.o'}"

		print(f"Compiling {output}")

		os.system(command)

def build_asm():
	for output in asm_files:
		command = "nasm -felf64"

		command += f" {output} -o build/{os.path.basename(output + '.o')}"

		print(command)
		print(f"Assembling {output}")

		os.system(command)

def link():
	command = "ld "

	for i in ld_flags:
		command += i + " "

	command += f"{' '.join([o for o in output_files])} -o kernel.elf"
  

	print(command)
	print(f"Linking kernel.elf")

	os.system(command)

def run():
	os.system("./scripts/make_image.sh")
	os.system(f"qemu-system-x86_64 -M q35 -m 2G -cdrom pyOS.iso")

if len(sys.argv) == 2:
    if sys.argv[1] == "clean":
        os.system("rm -rf build kernel.elf pyOS.iso")
        sys.exit(0)

build_py()
build_c()
build_asm()
link()
run()


