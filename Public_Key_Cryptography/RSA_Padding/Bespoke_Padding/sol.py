from pwn import * # pip install pwntools
from Crypto.Util.number import bytes_to_long as btl, long_to_bytes as ltb
from sage.all import * 
import json
import sys 
sys.set_int_max_str_digits(10**6)
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

N_list = []
CT_list = []
B_list = []
A_list = []
LEN = 10

for i in range(LEN):
    # NOPE
    pass

P = PolynomialRing(Zmod(product(N_list)), 'x')
x = P.gen()

f = P(0)

for i in range(LEN):
    crt_val = [0] * LEN
    crt_val[i] = 1
    T = crt(crt_val, N_list)
    f += T * ((A_list[i]*x + B_list[i]) ** 11 - CT_list[i])

f = f.monic()

rt = f.small_roots(X=2**(100*8), beta = 0.5)
print(rt)
