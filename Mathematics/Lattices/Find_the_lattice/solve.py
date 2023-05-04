from sage.all import *
from Crypto.Util.number import long_to_bytes as l2b
f = open('output.txt', 'r').readlines()
q, h = map(Integer, f[0].split(': ')[-1].strip()[1:-1].split(', '))
flag = int(f[1].split(': ')[-1].strip())
old_q, old_h = q, h
q = vector([xxx])
h = vector([xxx])


def Gaussian_Reduction(u, v):
    while True:
        if v.norm() < u.norm(): u, v = v, u
        m = round(u * v / (u * u))
        if m == 0: return u, v
        v = v - m * u
    pass


def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse_mod(f, g)) % g
    return m

p = Gaussian_Reduction(q, h)[0]

f, g = map(int, p)

print(l2b(decrypt(old_q, old_h, f, g, flag)))



