from pwn import *
from Crypto.Util.number import *
import json
import codecs

r = remote('socket.cryptohack.org', 13374, level = 'debug')

# Zadanie polega na tym, że serwer ma opcję sign, która signuje nasz input, signować to przecież znaczy `H(m)^d mod N`
# Serwer też ma opcje get_secret, która nam zwraca zaszyfrowaną flagę
# No ale jak ją odszyfrujemy tę flagę?
# Tu przychodzi nam z pomocą zrozumienie RSA bowiem, szyfrowanie to pow(plaintext, e, N), a deszyfrowanie to pow(ciphertext, d, N)
# deszyfrowanie to to samo co sign (z tym ze sign powinen być wykonany na hashu)
# wie generalnie to jak zrobimy na serwerze get_secret to dostaniemy x = pow(secret, e, N)
# i jak potem to wyślemy do sign to dostaniemy pow(x, d, N)
# czyli zauważ ze to to samo co deszyfrowanie, wiec serwer sam za nas zdeszyfruje flage

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

r.recvline()

json_send({"option": "get_secret"})

json_send({"option":"sign", "msg": json_recv()["secret"][2:]})

m = json_recv()["signature"][2:]

print(m)

print(bytes.fromhex(m))

r.interactive()