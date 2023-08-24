#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>

int main(){
    while(1){
        srand(time(0));
        int random_number = rand() % 417;
        printf("Random Number: %d\n", random_number);
        sleep(1);
    }
    return 0;
}
