from sage.all import *

v1 = vector((6, 2, -3))
v2 = vector((5, 1, 4))
v3 = vector((2, 7, 1))

M = matrix([v1, v2, v3])

print(abs(M.det()))