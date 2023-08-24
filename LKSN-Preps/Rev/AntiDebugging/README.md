# Anti Debugging

This is a technique to prevent debugging on the binary. This challenge is using `ptrace` to detects if the binary is on debug / trace mode.


## PTRACE
Indicate that this process is to be traced by its parent.
A process probably shouldn't make this request if its parent isn't expecting to trace it.  (pid, addr, and data are ignored.)

## How to detect?

```
➜   ./chall 
Welcome to main


➜   ltrace ./chall
ptrace(0, 0, 0, 0)  = -1
puts("Whoops Not allowed!"Whoops Not allowed! )  = 20
exit(1 <no return ...>
+++ exited (status 1) +++

```

## How to bypass?

Dynamic Approach:

1. GDB
    - Run GDB
    - break main or function that holds ptrace
    - use next instruction (`ni`) until you reach the ptrace function call.
    - `set $rax=0` if 64 bit or `set $eax=0` if 32 bit
    - continue (`c`) to resume the binary execution.

2. LD_PRELOAD: Will overwrite the ptrace function with our customed ptrace linker (.so) shared object

    - Create this file and save with `.so` extension
    ```
    long ptrace(int request, int pid, void *addr, void *data) {
        return 0;
    }
    ```
    - Compile with this command `gcc -shared ptrace.c -o ptrace.so`
    - Start GDB and insert this command `set environment LD_PRELOAD=./ptrace.so`

    ```
    gef➤  r
    Starting program: chall 
    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
    Whoops Not allowed!
    [Inferior 1 (process 8303) exited with code 01]
    gef➤  set environment LD_PRELOAD=./ptrace.so 
    gef➤  r
    Starting program: chall 
    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
    Welcome to main
    [Inferior 1 (process 8306) exited normally]

    ```

Static Approach:
- Disassemble :)