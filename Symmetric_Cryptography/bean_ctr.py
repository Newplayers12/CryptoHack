import requests as re
from pwn import xor
flag = bytes.fromhex(re.get('https://aes.cryptohack.org/bean_counter/encrypt/').json()['encrypted'])
print(flag)
blks = []
bag = set()
pt = bytes.fromhex('89504E470D0A1A0A0000000D49484452')
for i in range(0, len(flag), 16):
    block = flag[i * 16: (i + 1) * 16]
    blks.append(block)
    bag.add(block)


print(len(bag), len(blks))
key = xor(blks[0], pt)

f = open('answer.png', 'wb')

for i,x in enumerate(flag):
    # assert len(x) == 16, index
    
    f.write((x ^ key[i % len(key)]).to_bytes(1, 'big'))
f.close()

