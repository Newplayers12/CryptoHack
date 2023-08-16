from Crypto.Util.number import long_to_bytes as l2b, GCD
from sage.all import *
from gmpy2 import iroot
f = open('output.txt', 'r').readlines()

N = []
C = []
for line in f:
    if 'n' in line:
        N.append(int(line.split(' = ')[-1].strip()))
    elif 'c' in line:
        C.append(int(line.split(' = ')[-1].strip()))

if iroot(c, 3)[1]:
    print(l2b(int(iroot(c, 3)[0])))
        
