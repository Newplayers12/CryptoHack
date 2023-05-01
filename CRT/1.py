import math

ar = [5, 11, 17]
coe = [2, 3, 5]
N = math.prod(ar)
ans = 0
for i in range(len(ar)):
	Remain = N // ar[i]
	inv = pow(Remain, -1, ar[i])
	ans += inv * coe[i] * Remain
print(ans % N)