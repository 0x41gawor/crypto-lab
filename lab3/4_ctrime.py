import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long
import time
import string

# Jak działa kod za endpointem?
# Tu znowu mamy CTR (Counter mode decryption)
# losujemy IV
# robimy cipher AES w trybie CTR (wcześniej sami implementowaliśmy go, teraz uzywamy libki) counter inicjalizujemy IV
# na koniec to co wyjdzie z szyfrowania to kompresujemy razem z plaintext
def encrypt(plain):
    url = 'http://aes.cryptohack.org/ctrime/encrypt/'
    rsp = requests.get(url + plain + '/')
    return rsp.json()['ciphertext']

alphabet = '}'+'!'+'_'+'@'+'?'+string.ascii_uppercase+string.digits+string.ascii_lowercase

flag = b'crypto{'
cipher = encrypt(flag.hex())
mi = len(cipher)

while True:
    for c in alphabet:
        cipher = encrypt((flag+c.encode()).hex())
        print(c, len(cipher))
        if mi == len(cipher):
            flag += c.encode()
            mi = len(cipher)
            print(mi, flag)
            break
        if c == alphabet[-1]:
            mi += 2
            break
        time.sleep(1)

    if flag.endswith(b'}'): 
        print(flag)
        break