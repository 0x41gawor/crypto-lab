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

remote = remote('socket.cryptohack.org', 13380)

remote.recvuntil('Intercepted from Alice: ')
res = json_recv()
print(res) # Alice: p g A

p = int(res['p'], 16)
g = int(res['g'], 16)
A = int(res['A'], 16)

remote.recvuntil('Intercepted from Bob: ')
res = json_recv()
print(res) # Bob: B

B = int(res['B'], 16)

remote.recvuntil('Intercepted from Alice: ')
res = json_recv()
print(res) # Alice: iv i encrypted

iv = res['iv']
encrypted = res['encrypted']

# Mamy p,g,A,B. Musimy obliczyć b = pow(B, a, p), zeby jako Alice odszyfrować to co dał nam Bob
# Najpierw wiec jak widać musimy mieć `a`, które sobie Alice wymyśliła
# Wcześnij, gdy wiedzieliśmy ze Alice i Bob uzywaja multiplicative group, to wiedzieliśmy ze obliczenie a jest mega trudne
# W zasadzie to cały DH opiera się na tym, czyli na Discrete Logarithm Problem
# ale teraz skoro uzywają oni additive group, to `a` jest mega łatwo obliczyć
#  (zgodnie z zadaniem 1.) a = A * g^(-1) mod p (modular inverse) 
from Crypto.Util.number import inverse
a = A * inverse(g, p) % p
### więc teraz `b = B * a mod p` (a nie pow(B, a, p) jak do tej pory...)
shared_secret = B * a % p

print(decrypt_flag(shared_secret, iv, encrypted))