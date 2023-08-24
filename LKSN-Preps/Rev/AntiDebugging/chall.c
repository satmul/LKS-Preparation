#include <stdio.h>
#include <sys/ptrace.h>
#include <stdlib.h>

int main() {
    if (ptrace(PTRACE_TRACEME, 0, NULL, NULL) == -1) {
        printf("Whoops Not allowed!\n");
        exit(1);
    }
    printf("Welcome to main\n");
    return 0;
}