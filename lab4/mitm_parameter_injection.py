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
remote = remote('socket.cryptohack.org', 13371) 



print("=====================================")
print("Przechwycone w kierunku Alice---->Bob")
print("=====================================")
remote.recv() 
res = json_recv()
print(res)

print("=====================================")
print("Wysyłam do Boba to co od Alice ale moje: Oscar---->Bob")
print("=====================================")
remote.recv()
json_send({'p': hex(2), 'g': hex(2), 'A': hex(2)})

print("=====================================")
print("To dostałem od Boba w kierunku: Alice<----Bob")
print("=====================================")
remote.recv()
res = json_recv()
print(res)

### oszukujemy Alice, że 'B' Boba wynosi 1, dzięki czemu b, które sobie obliczy Alice = pow(B, a, p) = pow(1, a, p) = 1
print("=====================================")
print("Wysylam do Alice, ze niby B=1, więc ona sobie obliczy ze b=1: Oscar--->Alice")
print("=====================================")
remote.recv()
json_send({'B': hex(1)})

print("=====================================")
print("To dostałem od Alice w kierunku Boba: Alice---->Bob")
print("=====================================")
remote.recv()
res = json_recv()
print(res)
# Jak widać to co dostałem to (tak jak w dh_starter5.py) dict['iv','encrypted_flag']
# mogę to izi decryptować, bo wiem, że shared_secret = 1 (wymusiłem go)

shared_secret = 1
iv = res['iv']
ciphertext = res['encrypted_flag']

print(decrypt_flag(shared_secret, iv, ciphertext))

# Ten kod czasami działa a czasami nie XD to jest mega dziwne