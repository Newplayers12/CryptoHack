from Crypto.Util.number import isPrime

p = 28151
for number in range(2, p):
    f = set()
    for h in range(1, p):
        f.add(pow(number, h, p))
    if len(f) == p - 1: 
        print(number)
        break