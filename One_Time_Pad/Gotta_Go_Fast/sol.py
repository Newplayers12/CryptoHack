from pwn import * 
import json

r = remote('socket.cryptohack.org', 13372)
print(r.recv())

def json_recv():
    line = r.recv()
    print(line)
    return json.loads(line.strip().decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
    
json_send(send_flag)
data = json_recv()
flag = bytes.fromhex(data['encrypted_flag'])


json_send(send_data)
data = json_recv()


temp = bytes.fromhex(data['encrypted_data'])
pad = bytes.fromhex("ff"*len(flag))

r.close()

print(flag * pad * temp)




