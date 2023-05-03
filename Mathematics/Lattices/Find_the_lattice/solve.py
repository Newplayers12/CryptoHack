from sage.all import *

f = open('output.txt', 'r').readlines()
q, h = map(Integer, f[0].split(': ')[-1].strip()[1:-1].split(', '))
flag = f[1].split(': ')[-1].strip()



