import requests
from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
from Crypto.Util.number import long_to_bytes, bytes_to_long

# Co robi kod za tym endpointem?    
# Generuje cookie postaci admin=False;expiry={data+czas}"
# losuje jakiś IV do CBC
# szyfruje cookie za pomocą CBC i IV
# to co zwraca to IV + zaszyfrowane cookie
def get_cookie():
    url = "http://aes.cryptohack.org/flipping_cookie/get_cookie/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["cookie"])
# Co robi kod za tym endpointem?
# Odszyfrowuje cookie za pomocą podanego IV trybem CBC
# Patrzy czy w cookie admin=True
def check_admin(cookie, iv):
    url = "http://aes.cryptohack.org/flipping_cookie/check_admin/"
    url += cookie.hex()
    url += "/"
    url += iv.hex()
    url += "/"
    r = requests.get(url)
    js = r.json()
    print(js)

def xor(a, b):
    return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

# To co musimy zrobić w zadaniu to zdobyć cookie, wyciągnąć z niego IV i podmienić w nim `admin=False;` na `admin=True;`


cookie = get_cookie()
IV = cookie[:16]        # pierwsza część coookie to IV
block1 = cookie[16:32]
block2 = cookie[32:]

origin = b'admin=False;expi'
goal = b'admin=True;\x05\x05\x05\x05\x05'

new_IV = xor(xor(origin, goal), IV) # Podczas odszyfrowywania na koniec jest XOR z IV, zróbmy więc tak, że wyślemy do `check_admin` takie IV, że po XOR z znim 
                                     # ciphertext da plaintext w którym admin=True? Jak to zrobić XOR jest przemienienny, więc jak coś ^ coś wyszło admin=False
                                     # to jak to drugie coś XORniemy z admin=True, to potem z tym pierwszym XOR tak wyjdzie (właściwości XOR)

check_admin(block1, new_IV)