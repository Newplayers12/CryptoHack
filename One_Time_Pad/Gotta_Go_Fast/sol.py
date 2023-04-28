from pwn import * 
import json

r = remote('socket.cryptohack.org', 13372)
print(r.recv())


send_flag = {
    "option": "get_flag"
}


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

print(flag)

send_data = {
    "option": "encrypt_data",
    "input_data": "ff"*len(flag)
}

json_send(send_data)
data = json_recv()


temp = bytes.fromhex(data['encrypted_data'])
pad = bytes.fromhex("ff"*len(flag))

r.close()

print(xor(flag, xor(pad, temp)))




