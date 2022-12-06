import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

# OFB is an obscure cipher mode, with no real benefits these days over using CTR. This challenge introduces an unusual property of OFB.
# obscure - kept from being seen; concealed
# zrobienie z AES szyfry strumieniowego to po prostu to: The idea behind stream ciphers is to produce a pseudorandom keystream which is then XORed with the plaintext.

# Co robi kod za tym endpointem?
# Bierze plaintext i Initialization Vector
# następnie tworzy szyfr OFB (spójrz do AES.md) i za jego pomocą szyfruje plaintext
# OFB działa tak, ze AES robi się na IV i Key'u a na koniec to jest XOR'owane z plaintext i wychodzi ciphertext 
# potem następny blok do AES leci to co wyleciało z poprzedniego bloku 
def encrypt(plaintext, iv):
    url = "http://aes.cryptohack.org/symmetry/encrypt/"
    url += plaintext.hex()
    url += "/"
    url += iv.hex()
    url += "/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["ciphertext"])

# Co robi kod za tym endpointem?
# losuje jakiś IV i szyfruje flagę tak jak funkcja encrypt wyżej wywołana parametrami(flag, wylosowany IV)
# czyli to wyżej będzie nam służyć aby zgadnąć klucz, a tu dostaniemy zaszyfrowaną nim flagę
def encrypt_flag():
    url = "http://aes.cryptohack.org/symmetry/encrypt_flag/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["ciphertext"])

# W OFCB jest taka luka, ze plaintext ^ ciphertext zależy tylko od KEY i IV, a nie zależy od plaintext

def xor(a, b):
    return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

ciphered_flag = encrypt_flag()
iv = ciphered_flag[:16] # pierwsze 16bitów to IV
flag_enc = ciphered_flag[16:]   # reszta to zaszyfrowana flaga
l = len(flag_enc)

plaintext = b'\x00' * l # dajemy więc taki plaintext pusty i szyfrujemy go tym samym IV co została zaszyfrowana flaga

# następnie jak zrobimy XOR z tego co tu wyszło oraz zaszyfrowanej flagi to dostaniemy plaintext flagi
flag = xor(encrypt(plaintext, iv), flag_enc)

print(flag)