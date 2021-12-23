#!/bin/sh
rm -rf iso_root
mkdir -p iso_root
cp kernel.elf limine.cfg thirdparty/limine/limine.sys thirdparty/limine/limine-cd.bin thirdparty/limine/limine-eltorito-efi.bin iso_root/
xorriso -as mkisofs -b limine-cd.bin \
		-no-emul-boot -boot-load-size 4 -boot-info-table \
		--efi-boot limine-eltorito-efi.bin \
		-efi-boot-part --efi-boot-image --protective-msdos-label \
		iso_root -o pyOS.iso
	thirdparty/limine/limine-install pyOS.iso
	rm -rf iso_root


