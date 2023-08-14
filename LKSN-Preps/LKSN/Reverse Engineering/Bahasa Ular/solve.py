import this

filez = open("input_peserta","rb").read()

flag = ""
final = ""
for x in range(len(filez)):
	flag += chr(filez[x] ^ ord(this.s[x % len(filez)]))

for y in range(len(flag)):
	final += chr(ord(flag[y])^2^3^7^9^11^13)
print(flag)
print(final)