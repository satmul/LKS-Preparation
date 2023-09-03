# Solves multi prime rsa given n, e, and c. Need to factor n into primes first (recommend yafu)
# Reference https://crypto.stackexchange.com/questions/31109/rsa-enc-decryption-with-multiple-prime-modulus-using-crt
# From https://github.com/diogoaj/ctf-writeups/tree/master/2018/Timisoara/crypto/NotYourAverageRSA
from Crypto.Util.number import *
# Params
e = 65537
c = 94601003975036014892627558903765140006414154753639040877983052130842889430185826661689965123628679020897585326580781804995645118941447092101126138087372
n = 396024192066637812510450621382035407862868088296947670690301497371475295939904796980243233322894266141620734205143095605424207925368340802690646297450491
# primes are factored from n
primes = [2520734081,2963163041,2968229111,3010828267,3170708137,3256290119,3356156009,3368813909,3468273229,3671092039,3679173373,3760110227,4012932073,4076280259,4135959361,4264770803]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

ts = []
xs = []
ds = []

for i in range(len(primes)):
	ds.append(modinv(e, primes[i]-1))

m = primes[0]

for i in range(1, len(primes)):
	ts.append(modinv(m, primes[i]))
	m = m * primes[i]

for i in range(len(primes)):
	xs.append(pow((c%primes[i]), ds[i], primes[i]))

x = xs[0]
m = primes[0]

for i in range(1, len(primes)):
	x = x + m * ((xs[i] - x % primes[i]) * (ts[i-1] % primes[i]))
	m = m * primes[i]

print(hex(x%n)[2:-1])