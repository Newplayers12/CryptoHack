from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import isPrime
from math import gcd
N_list = []
for i in range(1, 51):
    with open(f'keys_and_messages/{i}.pem', 'r') as f:
        key = RSA.importKey(f.read())
    N_list.append(key.n)
    if (i == 20): print(key.e)
    # cipher = PKCS1_OAEP.new(key)
    



for i, u in enumerate(N_list):
    for j, v in enumerate(N_list):
        if i != j and gcd(u, v) != 1:
            print(i, j)


p = gcd(N_list[20], N_list[33])
q = N_list[20] // p


key = RSA.construct((N_list[20], 65537, pow(65537, -1, (p - 1) * (q - 1))))
cipher = PKCS1_OAEP.new(key) 

flag = bytes.fromhex(open(f"keys_and_messages/21.ciphertext", 'r').read())
print(cipher.decrypt(flag))

