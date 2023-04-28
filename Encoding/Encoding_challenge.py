from pwn import *
import json
import base64
import codecs


r = remote('socket.cryptohack.org', 13377)

for _ in range(100):
    data = r.recv().strip()

    data = json.loads(data)
    
    flag = data['encoded']

    if data['type'] == 'base64':
        flag = base64.b64decode(flag).decode()
    elif data['type'] == 'rot13':
        flag = codecs.decode(flag, 'rot-13')
    elif data['type'] == 'hex':
        flag = codecs.decode(flag, 'hex').decode()
    elif data['type'] == 'bigint':
        flag = bytes.fromhex(flag[2:]).decode()
    elif data['type'] == 'utf-8':    
        flag = ''.join([chr(int(x)) for x in flag])


    send = {
        "decoded": flag
    }

    r.sendline(json.dumps(send).encode())

print(r.recv())



print("================================")