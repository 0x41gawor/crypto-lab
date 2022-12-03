# ----------------------------------------D E C R Y P T----------------------------------- # obsługa decyrptowania wiadomości AES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import json
from pwn import *


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
# ----------------------------------------D E C R Y P T-----------------------------------
# ---------------------------------- J S O N    D E R U L O ------------------------------- #obsługa recv i send jsonów
def json_recv():
    line = remote.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    remote.sendline(request)
# ---------------------------------- J S O N    D E R U L O -------------------------------

# Connect at nc socket.cryptohack.org 13371
remote = remote('socket.cryptohack.org', 13373)

remote.recv()
res = json_recv()
print(res) # dostajemy p g i A, skoro duże A to wiemy że od Alice

p = int(res['p'], 16)
g = int(res['g'], 16)
A = int(res['A'], 16)

print("BOB")

remote.recvuntil('Intercepted from Bob: ')
res = json_recv()
print(res) # od Boba: B

B = int(res['B'], 16)

remote.recvuntil('Intercepted from Alice: ')
res = json_recv()
print(res) # Od Alice: iv oraz encrypted

iv = res['iv']
encrypted = res['encrypted']

# do wywołania print(decrypt_flag(shared_secret, iv, encrypted_flag)) potrzebujemy shared_secret czyli b=pow(B,a,p)

# Wysylam Bobowi jako Alice p,g,A, ale A daje 1, a g daje jako A
remote.recvuntil('send him some parameters: ')
json_send({'p': hex(p), 'g': hex(A), 'A': hex(1)})

# Bob wysyła mi B, czyli pow(g,a,p)
remote.recvuntil('Bob says to you: ')
res = json_recv()
print(res)

# ale to co on mi wysyłał jako niby B, to tak naprawde jest `b` czyli jego secret, któego ja używam aby sobie decryptować flage
shared_secret = int(res['B'], 16)

### odszyfrowanie flagi
print(decrypt_flag(shared_secret, iv, encrypted))