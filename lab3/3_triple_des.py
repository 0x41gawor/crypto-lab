import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

# Co robi kod za endpointem?
# Jako input bierze nasz klucz i plaintext i szyfruje - zwraca ciphertext
# Ale jak szyfruje?
# najpierw plaintext XOR'uje z wylosowanym IV
# potem zagania do pracy algorytm DES i znim szyfruje plaintext
# następnie zaszyfrowany plaintext, czyli ciphertext xoruje z IV znowu
def encrypt(key, plaintext):
    url = "http://aes.cryptohack.org/triple_des/encrypt/"
    url += key.hex()
    url += "/"
    url += plaintext.hex()
    url += "/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["ciphertext"])

# Co robi kod za endpointem?
# podajemy tu klucz, a funkja bierze flagę i razem z podanym przez nas kluczem wysyła do fcji wyżej
# przy okazji flagę paduje do wielokrotności 8
def encrypt_flag(key):
    url = "http://aes.cryptohack.org/triple_des/encrypt_flag/"
    url += key.hex()
    url += "/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["ciphertext"])

# DES ma powazną insecurity albowiem jest weak key
# https://en.wikipedia.org/wiki/Data_Encryption_Standard
# Encryption (E) and decryption (D) under a weak key have the same effect (see involution)
# An involution is a function that, when applied twice, brings one back to the starting point.
# Szyfrowanie i deszyfrowanie to te same operacje
# Więc w zadaniu wystarczy że zaszyfrujemy flagę jakimkolwiek kluczem, i potem to co dostaniemy to zaszyfrujemy znowu tym samym kluczem

# Bierzemy sobie jakiś pusty ciphertext jak w poprzednim zadaniu
ciphertext = b"\x00" * 32

weak_key = [b"\x00" * 8, b"\xff" * 8] # wymyślamy sobie jakiś klucz 000...fff....

key = weak_key[0] + weak_key[1]

step1 = encrypt_flag(key) # używamy tego klucza zeby zaszyfrować flagę 
step2 = encrypt(key, step1) # teraz robimy szyfrowanie jeszcze raz, a zaaplikowane szyfrowanie drugi raz zwróci nam to co było zaszyfrowane czyli flagę 

print(step2)