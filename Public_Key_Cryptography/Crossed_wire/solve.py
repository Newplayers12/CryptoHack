from Crypto.Util.number import GCD, isPrime, long_to_bytes as l2b
from Crypto.Random.random import randint
from math import prod


def factor_Phi(N, e, d):
    k = e * d - 1
    while True:
        r = 0
        while not (k & 1):
            k >>= 1
            r += 1
        g = randint(2, N - 1)
        if 1 < GCD(g, N) < N:
            return g
        x = pow(g, k, N)
        for _ in range(r):
            y = GCD(x - 1, N)
            if 1 < y < N:
                return y
            x = x * x % N
    
        

f = open('output.txt', 'r').readlines()

N, d = map(int, f[0].split(': ')[-1][1:-2].split(', '))

print(N, d)

p = factor_Phi(N, 0x10001, d)
assert isPrime(p)
q = N // p
assert isPrime(q)

primes = []

primes = list(filter(
                        lambda x: x, 
                        f[1].split(': ')[-1][2:-3]
                        .replace(str(N), '').replace('(', '')
                        .replace(')', '').split(', ')
                    ))


primes = list(map(int, primes))

ps = prod(primes)
ds = pow(ps, -1, (p - 1)*(q - 1))
print(ds)

ct = int(f[2].split(': ')[-1][:-1])
print(l2b(pow(ct, ds, N)))