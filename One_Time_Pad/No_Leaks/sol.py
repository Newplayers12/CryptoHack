from pwn import * 
import json
import time
import base64

r = remote('socket.cryptohack.org', 13370)
print(r.recv())

def json_recv():
    line = r.recv()
    return json.loads(line.strip().decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


while True:    
    
    json_send({"msg": "request"})
    data = json_recv()
        
    if 'ciphertext' in data:
        b = base64.b64decode(data['ciphertext'])
        """
            MAGIC
        """
    
    
    """
        MAGIC
    """



r.close()






