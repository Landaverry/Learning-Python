#Python - Introduction to pwntools
#pwntools is a exploit development library that can be very useful for hacking scripts
from pwn import *
#Buffer overflow cyclic function
print(cyclic(50))
print(cyclic_find("laaa"))

#Working directly with shellcode
print(shellcraft.sh())
#Print as assembly langauge
print(hexdump(asm(shellcraft.sh())))

#Starting a process
p = process("/bin/sh")
p.sendline("echo hello;")
p.interactive()
p.close()

#Interacting with a remote process
#r = remote("127.0.0.1",1234)
#r.interactive()
#r.close()

#Packing and unpacking numbers
print(p32(0x13371337))
print(hex(u32(p32(0x13371337))))

#Load files
l = ELF('/bin/bash')
print(hex(l.address))
print(hex(l.entry))
print(hex(l.got['write']))
print(hex(l.plt['write']))

#Search directly in an ELF file 
for address in l.search(b'/bin/sh\x00'):
	print(hex(address))

print(next(l.search(asm('jmp esp'))))
print(hex(next(l.search(asm('jmp esp')))))
#Search for rbx gadget
r=ROP(l)
print(r.rbx)
#Encryption & Hashinf functions
print(xor("A","B"))
#Base64 encoding
print(b64e(b'test'))
#Base64 Decoding
print(b64d(b"dGVzdA=="))
#md5 Hash summing
print(md5sumhex(b"hello"))
#SHA-1 hash summing
print(sha1sumhex(b"hello"))
#