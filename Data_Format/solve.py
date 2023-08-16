from Crypto.PublicKey import RSA

key = RSA.import_key(open('privacy_enhanced_mail.pem', 'r').read())
print(key.d)

key = RSA.import_key(open('bruce_rsa.pub', 'r').read())
print(key.n)


# flag = "Bxxxxxxxxxxxxxxxxxxxxxx79BXXXXXXXXXXXXXXXXXXXXXXX859"
# print(int(flag, 16))