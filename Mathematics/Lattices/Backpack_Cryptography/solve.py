from sage.all import *
f = open("output.txt", "r").readlines()

M = list(map(int, f[0].split(': ')[-1][1:-2].split(', '))) # extracted M

S = int(f[1].split(': ')[-1].strip())

n = len(M)
temp = [[0 for i in range(n + 1)] for j in range(n + 1)]


M = matrix(ZZ, temp)
ans = """MAGIC"""

print(ans * M.inverse())

ans = ("nope", 0, "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", 0, "nope", "nope", 0, 0, "nope", "nope", "nope", 0, 0, 0, 0, 0, "nope", "nope", "nope", 0, 0, 0, "nope", 0, "nope", "nope", 0, 0, 0, "nope", "nope", "nope", 0, "nope", "nope", 0, "nope", "nope", 0, "nope", 0, "nope", "nope", 0, "nope", "nope", "nope", "nope", "nope", 0, "nope", 0, "nope", 0, 0, "nope", "nope", "nope", "nope", 0, "nope", 0, "nope", "nope", 0, "nope", "nope", 0, "nope", "nope", 0, "nope", -1, -1, -1, 0, -1, -1, -1, -1, 0, -1, -1, 0, 0, 0, -1, 0, -1, -1, -1, 0, 0, 0, 'nope')
b = 0
for i, x in enumerate(ans):
    if x:
        b &= 1<<i
        
from Crypto.Util.number import long_to_bytes as l2b
print(l2b(b))




