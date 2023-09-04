import random
import os

def randomisasi(benih):
	random.seed(benih)
	x = random.randint(0,9032)
	return x


def main():
	user = int(input("masukkan benih keberuntungan hari ini: "))
	number = randomisasi(user)
	if (number == 1337):
		print("FLAG{placeholder}")
	else:
		print("coba lagi, anda kurang beruntung")


main()


#36313
#Seed is used to initialize random number generator (RNG)
#RNG is using time as their default thing.
#If seed is used, then the RNG is always be the same.