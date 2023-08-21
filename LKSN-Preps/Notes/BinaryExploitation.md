# Finding libc file

`ldd [binary]`

```
ldd vuln-64 
        linux-vdso.so.1 (0x00007ffcfa726000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fa4699bc000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fa469bbc000)

```

# Patching binary

If the challenge provide the libc.so.6 or ld files you could patch the binary with `pwninit` and `patchelf`

- Install patchelf (`apt-get install patchelf`)
- Download pwninit (https://github.com/io12/pwninit/releases)

Patch with `/opt/pwninit --bin [binary] --libc [libc.so.6] --ld [ld file]`

# Find leak(s)

- Search usable GOT and PLT
- Calculate the offset of the leaked GOT (leak - libc.symbols["puts"]) and set `libc.address`
- Find the str_bin_sh and system
- Recheck the address with `pause()` and `x/s [address]`
  - libc base address: ELF
- Return to main again to send the attack payload `padding + ret + bin_sh + system`
