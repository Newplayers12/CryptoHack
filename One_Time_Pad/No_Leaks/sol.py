from pwn import * 
import json
import time

r = remote('socket.cryptohack.org', 13370)
print(r.recv())

def json_recv():
    line = r.recv()
    return json.loads(line.strip().decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:    
    start = time.time()
    json_send({"msg": "request"})
    data = json_recv()
    
    print(time.time() - start)
    if 'ciphertext' in data:
        print(data['ciphertext'])
    
    




r.close()






