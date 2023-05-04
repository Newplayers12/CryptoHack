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
    
# flag = b'c'b'r'b'y'b'p'b't'b'o'b'{'b'u'b'n'b'r'b'4'b'n'b'd'b'0'b'm'b'_'b'0'b'7'b'p'b'}'


r.close()






