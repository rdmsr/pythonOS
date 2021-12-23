#!/usr/bin/env python
import os

os.system('rm -rf iso_root')
os.system('mkdir -p iso_root')
os.system('cp kernel.elf limine.cfg thirdparty/limine/limine.sys thirdparty/limine/limine-cd.bin thirdparty/limine/limine-eltorito-efi.bin iso_root/')

os.system("xorriso -as mkisofs -b limine-cd.bin -no-emul-boot -boot-load-size 4 -boot-info-table --efi-boot limine-eltorito-efi.bin -efi-boot-part --efi-boot-image --protective-msdos-label iso_root -o pyOS.iso")

os.system('thirdparty/limine/limine-install pyOS.iso')
os.system('rm -rf iso_root')


