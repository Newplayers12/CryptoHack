from sage.all import *

v = vector((846835985, 9834798552))
u = vector((87502093, 123094980))


def Gaussian_Reduction(u, v):
    while True:
        if v.norm() < u.norm(): u, v = v, u
        m = round(u * v / (u * u))
        if m == 0: return u, v
        v = v - m * u
    pass

p, q = Gaussian_Reduction(u, v)

print(p * q)
