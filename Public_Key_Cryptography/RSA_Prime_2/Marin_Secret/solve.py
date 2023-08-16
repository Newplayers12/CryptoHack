from Crypto.Util.number import isPrime, long_to_bytes as l2b
f = open('output.txt', 'r').readlines()

n, e, c = map(int, [f[i].split()[-1] for i in range(3)])
print(n)
cnt = 2
while n % ((1<<cnt) - 1):
    cnt += 1
    

p = (1<<cnt) - 1
q = n // p
assert isPrime(p) and isPrime(q)
d = pow(e, -1, (p - 1) * (q - 1))
print(l2b(pow(c, d, n)))
