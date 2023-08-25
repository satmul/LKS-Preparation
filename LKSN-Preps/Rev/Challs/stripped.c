#include <stdio.h>
#include <string.h>

char flag(){
	char kunci[] = "SMKN1_CIMAHI";
	char input[30];
	char flag[] = {0x0f,0x04,0x00,0x0a,0x32,0x2e,0x3e,0x5f,0x3a,0x2a,0x3d,0x0c,0x22,0x29,0x2d,0x24,0x28,0x2d,0x00,0x5a,0x2b,0x39,0x28,0x3d,0x34};
	scanf("%s",input);
	if(strcmp(input,strrev(kunci))==0){
		int x=0;
		for(x;x<25;x++){
			printf("%c",kunci[x%12]^flag[x]);
		}
	}
	else{
		printf("nicetry");
	}
}

int main(){
	printf("Ini adalah stripped binary..\n");
	printf("Input kunci rahasia untuk dapat flagnya: ");
	flag();
	return 0;
}
