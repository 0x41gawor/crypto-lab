from Crypto.PublicKey import RSA

f = open('input.pem','r')
key = RSA.import_key(f.read())


print(key)