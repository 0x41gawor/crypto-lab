from pwn import *
from Crypto.Util.number import *
import json
import codecs

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import math
import sympy
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

remote = remote('socket.cryptohack.org', 13378)

remote.recvuntil("Intercepted from Alice: ")
res = json_recv()
p = int(res["p"], 16)
g = int(res["g"], 16)
A = int(res["A"], 16)

remote.recvuntil("Intercepted from Bob: ")
res = json_recv()
B = int(res["B"], 16)

remote.recvuntil("Intercepted from Alice: ")
res = json_recv()
iv = res["iv"]
ciphertext = res["encrypted"]


# Mamy p,g,A,B ale tym razem wysłanie Bobowi `g=prawdziwe A` i A=1 nie zmyliło Boba
# Trzeba wymyśleć coś lepszego 
# Może po prostu wyślemy mu takiego p, żeby łatwo było z DLP obliczyć jego `b`
# czyli wcześniej ten cep nam wysłał sam `b`, a teraz lurniemy go tak, aby on wyslal nam cos, zeby nam bylo ez obliczyc `b`
# https://susanou.github.io/Writeups/posts/static-client2/
# DLP latwo sie liczy na niektórych liczbach pierwszych, tu mamy funkcje, ktora nam generuje takie 'smooth_prime'
def smooth_p():
    mul = 1
    i = 1
    while 1:
        mul *= i
        if (mul + 1).bit_length() >= 1536 and isPrime(mul + 1):
            return mul + 1
        i += 1
# teraz po prostu uzywamy tej funkcji, zeby zrobić `p`, ale w wersji smooth
s_p = smooth_p()
# tak jak poprzednio wysylamy Bobowi oszukawcze p,g,A
remote.recvuntil("send him some parameters: ")
json_send({
    "p": hex(s_p),
    "g": hex(2),
    "A": hex(A)
    })

remote.recvuntil("Bob says to you: ")
res = json_recv()
B = int(res["B"], 16)
# on nam odpowiada swoim public `B`, które wygenerował na podstawie naszego smooth p
# więc teraz my obliczymy jakie jest jego `private p`
print("Obliczanie")
b = sympy.ntheory.residue_ntheory.discrete_log(s_p, B, 2) # g dalismy 2 wyzej

# końcówka taka jak zawsze
shared_secret = pow(A,b,p) # czyli `a`

print(decrypt_flag(shared_secret, iv, ciphertext))