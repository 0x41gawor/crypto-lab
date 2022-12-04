import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

# Co robi kod za tym endpointem?
# Sprawdza czy klucz jaki my zgadujemy ze został użyty do szyfrowania AES został rzeczywiście użyty
# Jeśli zgadywany przez nas klucz jest prwadziwy to zwraca nam flage
def get_flag(key):
    url = "http://aes.cryptohack.org/lazy_cbc/get_flag/"
    url += key.hex()
    url += "/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["plaintext"])

# Tutaj wysyłamy zaszyfrowany tekst a dostajemy plaintext (to co w kodzie jest decrypted.hex())
# Co warto zauważyć to to, że jako IV zamiast losowany to jest brany KEY

def receive(ciphertext):
    url = "http://aes.cryptohack.org/lazy_cbc/receive/"
    url += ciphertext.hex()
    url += "/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["error"][len("Invalid plaintext: "):])

def xor(a, b):
    return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

# Wymyślam sobie jakiś pusty ciphertext
ciphertext = b"\x00" * 32               # Dostałem z tego b'beae59cd86a38d7dcaa70bfc55679e9e49a0b2f027f0133ff783b0b9e1031d77' - dwa bloki po 16bajtów

# Zauważmy, że w poprzednich zadaniach umieliśmy wyciągnąć IV no to teraz też umiemy, tyle zę w tym przypadku IV jest również kluczem :D
plaintext1plaintext2 = receive(ciphertext)
plaintext1 = plaintext1plaintext2[:16]
plaintext2 = plaintext1plaintext2[16:]

# Jak popatrzymy na rysunek tu: http://aes.cryptohack.org/lazy_cbc/
# To nam wyjdą takie równania:
# plaintext1 = KEY ^ decrypted(b"\x00" * 32)
# plaintext2 = plain(b"\x00" * 32) ^ decrypted(b"\x00" * 32)
# Jak zrobimy trochę przekształceń i właściwości XOR to wyjdzie:
# KEY = plaintext1 ^ plaintext2
# https://onealmond.github.io/ctf/cryptohack/lazy-cbc.html
key = xor(plaintext1, plaintext2)
print(get_flag(key))