# ----------------------------------------D E C R Y P T----------------------------------- # obsługa decyrptowania wiadomości AES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import json
import sympy
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


# --------------------------------------------------------------------------------------T A S K   S P E C I F I C   C O D E   B E G I N S   H E R E ------------------
remote = remote('socket.cryptohack.org', 13379)

print("=====================================")
print("Przechwycone w kierunku Alice---->Bob")
print("=====================================")
remote.recv() 
res = json_recv()
print(res) # Jak se to printłem to widze po liczbach ze to rózne typy algorytmu Diffie-Hellmans, więc oszukam Bob'a, żeby zrobił 64 bo to izi


print("=====================================")
print("Wysyłam do Bob'a ze niby tylko DH64 Alice wspiera: Oscar--->Bob")
print("=====================================")
remote.recv() 
json_send({'supported': ['DH64']})


remote.recv() 
res = json_recv()
# print(res)
# Bob mi wysłał, że wybral DH64, też mu wyśle jako niby Alice ze wybieram Dh64
remote.recv() 
json_send({'chosen': 'DH64'})

print("=====================================")
print("Przechwytuje od Alice takie {p,g,A}: Alice--->Bob")
remote.recv() 
res = json_recv()
print(res)

# zamieniam je sobie na system dziesietny
p = int(res['p'], 16)
g = int(res['g'], 16)
A = int(res['A'], 16)

print("=====================================")
print("Przechwytuje od Boba: Alice<---Bob")
remote.recvuntil('Intercepted from Bob: ') # nie czaje zemu tak, ale to dziala a inne nie
res = json_recv()
print(res)

B = int(res['B'], 16) # zamieniam jego B na liczbe w systemie dziesietnym

print("=====================================")
print("Przechwytuje od Alice: Alice--->Bob")
remote.recvuntil('Intercepted from Alice: ')
res = json_recv()
print(res)

iv = res['iv']
encrypted_flag = res['encrypted_flag']

# Doszliśmy w końcu do fazy gdzie Alice wysyła wiadomość, nie oszukiwałem tu nikogo nic jak w poprzednim zadaniu
# Mimo, to możemy łatwo znaleźć `a` jakiego użyła Alice do zrobienia dużego `A`
# Tak się składa, że można je obliczyć rozwiązując DLP (Discrete Logarithm Problem) i przy nieodpowiednim doborze parametrów DH jest to łatwe 
# Dlatego oszukaliśmy te 64bity, bo łatwo to rozwiązać
a = sympy.ntheory.residue_ntheory.discrete_log(p, A, g)
### obliczamy b = pow(B, a, p)
shared_secret = pow(B, a, p)

print(decrypt_flag(shared_secret, iv, encrypted_flag))