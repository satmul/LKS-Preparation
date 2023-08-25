#include <stdio.h>
#include <string.h>
#include <windows.h> //windows
//#include <unistd.h>


char* flag_1(){
	return "FLAG{FLAG_1_ternyata_ada_di_function}";
}

int main(){
	int choice;
	char flag[]={0x2d,0x7c,0x72,0x29,0x2b,0x58,0x12,0x31,0x13,0x5c,0x37,0x5d,0x1d,0x00,0x3e,0x13,0x5f,0x41,0x31,0x13,0x0f,0x04,0x36,0x1c,0x53,0x15};
	
	char kunci[30];
	printf("Haloo, flagnya dimana ya?\n");
	printf("Disini ada 3 flag yang bisa didapatkan!\n\n\n");

	printf("1. Challenge 1\n");
	printf("2. Challenge 2\n");
	printf("3. Challenge 3\n");
	printf("Input: ");
	scanf("%d",&choice);
	switch(choice){
		case 1:
			printf("Flagnya disitu dah pokoknya.");
			break;
		case 2:
			printf("Input kunci rahasia milik admin:");
			scanf("%s",kunci);
			if(strcmp(kunci,"k03ntji_r4h4sia") == 0){
				int x=0;
				for(x;x<26;x++){
					printf("%c",kunci[x%15]^flag[x]);
				}

				printf("\nSelamat, Flag 2 sudah ditemukan.");
			}
			else{
				printf("Coba lagi, jangan menyerah.");
			}
			break;
		case 3:
			printf("Oke aku akan berikan flag secara gratis, tapi tunggu sebentar...\n");
			printf("Aku kirimkan per karakter ya!\n");

			puts("F");
			sleep(1);
			puts("FL");
			sleep(2);
			puts("FLA");
			sleep(3);
			puts("FLAG");
			sleep(1);
			puts("FLAG_");
			sleep(1);
			puts("FLAG_3");
			sleep(1);
			puts("FLAG_3{");
			sleep(2);
			puts("FLAG_3{b");
			sleep(3);
			puts("FLAG_3{b3");
			sleep(1);
			puts("FLAG_3{b3r");
			sleep(1);
			puts("FLAG_3{b3r5");
			sleep(2);
			puts("FLAG_3{b3r5a");
			sleep(2);
			puts("FLAG_3{b3r5ab");
			sleep(2);
			puts("FLAG_3{b3r5ab4");
			sleep(2);
			puts("FLAG_3{b3r5ab4R");
			sleep(3);
			puts("FLAG_3{b3r5ab4Rl");
			puts("[!] Disconnected.......");
			sleep(138832990);
			puts("FLAG_3{b3r5ab4Rla");
			sleep(2);
			puts("FLAG_3{b3r5ab4RlaH");
			sleep(5);
			puts("FLAG_3{b3r5ab4RlaH}");
			sleep(0.5);

			break;
		default:
			printf("Jangan coba-coba :<\n");
	}
}



