def find_date():
    for y in range(0, 2023):
        for m in range(1, 13):
            for d in range(1, 32):
                if (y) * (m) * d == 28077:
                    print(f"y = {y}, m = {m}, d = {d}")


find_date()
key = [1337,3,7]

enc = [1371,48,117,1363,55,107,1293,109,88,1373,106,88,1364,48,35,1288,109,88,1358,55,108,1357,118]
print(key)
flag = ""
for x in range(len(enc)):
    flag += chr(key[x%3]^(enc[x]))

print(str(len(flag))+":"+flag)