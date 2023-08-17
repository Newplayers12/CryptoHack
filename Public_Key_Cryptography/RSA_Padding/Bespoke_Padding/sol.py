from pwn import * # pip install pwntools
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from sage.all import * 
from decimal import Decimal
import json

r = remote('socket.cryptohack.org', 13386)
r.recv()
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


json_send({"option": "get_flag"})


data = json_recv()
r.close()
ct = int(data['encrypted_flag'])
N = int(data['modulus'])
a, b = map(int, data['padding'])

def func(N, ct, a, b):
    P = PolynomialRing(Zmod(N), 'x', implementation='NTL')
    (x, ) = P.gens()
    beta = 0.4
    B=b'crypto{'+ (b'\x00'*27) +b'}'
    f = ((a*(b2l(B) + x*256) + b)**11 - ct)//((a * 256)**11)
    dd = f.degree()    # Degree of the polynomial
    epsilon = 1/30 # magic
    # XX = pow(N, (beta**2/dd) - epsilon)
    # XX = int(XX)
    rt = f.small_roots( epsilon=epsilon)
    return rt
print(func(N, ct, a, b))