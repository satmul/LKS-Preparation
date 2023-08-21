# Reverse Engineering (https://ctf101.org/reverse-engineering)

## Assembly

Source Code


```
#include <stdio.h>

int main(){
    int a = 10;
    int b = 20;

    printf("Hello World");
    return 0;
}
```


Assembly

```
.LC0:
        .string "Hello World"
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     DWORD PTR [rbp-4], 10
        mov     DWORD PTR [rbp-8], 20
        mov     edi, OFFSET FLAT:.LC0
        mov     eax, 0
        call    printf
        mov     eax, 0
        leave
        ret
```

## Register

![](register.png)

Perbedaan hanya ada di awal register, sisanya mirip sama..

![](multi-register.png)

1. ### Instruction

- Data movement: mov rax, [rsp - 0x02]
- Arithmetic: add rax, rbx
- Control-flow: jne 0x8000300


2. ### Execution

```
RIP --->    0x0804000: mov eax, 0x10                  Register Values:
            0x0804005: mov ebx, 0x2                   RIP = 0x0804000
            0x080400a: add, rax, rbx                  RAX = 0x0
            0x080400d: inc rbx                        RBX = 0x0
            0x0804010: sub rax, rbx                   RCX = 0x0
            0x0804013: mov rcx, rax                   RDX = 0x0
```

```
            0x0804000: mov eax, 0x10                  Register Values:
RIP --->    0x0804005: mov ebx, 0x2                   RIP = 0x0804005
            0x080400a: add, rax, rbx                  RAX = 0x10
            0x080400d: inc rbx                        RBX = 0x0
            0x0804010: sub rax, rbx                   RCX = 0x0
            0x0804013: mov rcx, rax                   RDX = 0x0
```

```
            0x0804000: mov eax, 0x10                  Register Values:
            0x0804005: mov ebx, 0x2                   RIP = 0x080400a
RIP --->    0x080400a: add, rax, rbx                  RAX = 0x10
            0x080400d: inc rbx                        RBX = 0x2
            0x0804010: sub rax, rbx                   RCX = 0x0
            0x0804013: mov rcx, rax                   RDX = 0x0
```

```
            0x0804000: mov eax, 0x10                  Register Values:
            0x0804005: mov ebx, 0x2                   RIP = 0x080400d
            0x080400a: add, rax, rbx                  RAX = 0x12
RIP --->    0x080400d: inc rbx                        RBX = 0x2
            0x0804010: sub rax, rbx                   RCX = 0x0
            0x0804013: mov rcx, rax                   RDX = 0x0
```


```
            0x0804000: mov eax, 0x10                  Register Values:
            0x0804005: mov ebx, 0x2                   RIP = 0x0804010
            0x080400a: add, rax, rbx                  RAX = 0x12
            0x080400d: inc rbx                        RBX = 0x3
RIP --->    0x0804010: sub rax, rbx                   RCX = 0x0
            0x0804013: mov rcx, rax                   RDX = 0x0
```
```
            0x0804000: mov eax, 0x10                  Register Values:
            0x0804005: mov ebx, 0x2                   RIP = 0x0804013
            0x080400a: add, rax, rbx                  RAX = 0x9
            0x080400d: inc rbx                        RBX = 0x3
            0x0804010: sub rax, rbx                   RCX = 0x0
RIP --->    0x0804013: mov rcx, rax                   RDX = 0x0
```

```
            0x0804000: mov eax, 0x10                  Register Values:
            0x0804005: mov ebx, 0x2                   RIP = 0x080400a
            0x080400a: add, rax, rbx                  RAX = 0x9
            0x080400d: inc rbx                        RBX = 0x3
            0x0804010: sub rax, rbx                   RCX = 0x9
            0x0804013: mov rcx, rax                   RDX = 0x0
```

3. ### Control Flow (https://faydoc.tripod.com/cpu)

- jnz (Jump Not Zero)
- jz (Jump equal)
- jge (Jump greater)
- jle (Jump less or equal)
- jl (Jump less)
- ....


4. ### Address 

```
mov rax, [0xabababab] === rax = *0xabababab
```


# GDB (Gnu Debugger - GEF)

### Execute
```
gdb [./binary]
```

### Disassemble Binary
```
gdb disass [symbol / function name] => gdb disass main

or 

gdb disass *[address] => gdb disass *0x7fffaaaa
```

### View Instructions (https://visualgdb.com/gdbreference/commands/x)
```
[display_format]/[lines]i [address] [+- offset]

x/10i (display 10 lines of instruction in hex format)
gef➤  x/10i    0x00000000004011d0
                0x4011d0 <_start>:   endbr64
                0x4011d4 <_start+4>: xor    ebp,ebp
                0x4011d6 <_start+6>: mov    r9,rdx
                0x4011d9 <_start+9>: pop    rsi
                0x4011da <_start+10>:        mov    rdx,rsp
                0x4011dd <_start+13>:        and    rsp,0xfffffffffffffff0
                0x4011e1 <_start+17>:        push   rax
                0x4011e2 <_start+18>:        push   rsp
                0x4011e3 <_start+19>:        mov    r8,0x401640
                0x4011ea <_start+26>:        mov    rcx,0x4015d0
```


### Setting Breakpoint
```
break *address (+- offset)
or
break function
```

### Interacting with instructions
```
1. Stepping
- Continue: Resume the execution of program after break point(s) [default: c]
- Step Into: Step into number(s) of interactions [default: s (one instruction)]
- Next Instruction / step over: Jump into the next instruction (skipping the instruction)
- Finish: Finish the execution of the binary after return.
```