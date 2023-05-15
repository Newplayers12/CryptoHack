from pwn import * # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13371)

r.recvuntil(b'Intercepted from Alice: ')

def json_recv():
    line = r.recvline()
    print(line)
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
    
    
data = json_recv()
g = int(data['g'][2:], 16)
A = int(data['A'][2:], 16)
p = int(data['p'][2:], 16)

c = 123
C = pow(g, c, p)

send_data = {
    "g": hex(g),
    "A": hex(C),
    "p": hex(p)
}
json_send(send_data)

r.recv()
r.recv()
data_Bob = json_recv()

print(data_Bob)

B = int(data_Bob['B'][2:], 16)

send_data = {
    "B": hex(C)
}
json_send(send_data)


r.recvuntil(b'Intercepted from Alice: ')
data = json_recv()

import decrypt_AES 

shared_secret = pow(A, c, p)

print(decrypt_AES.decrypt_flag(shared_secret, *data.values()))

r.close()
    
    

    
    
    
