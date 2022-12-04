import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long
# Zamiast przepisywać ten kodzik http://aes.cryptohack.org/ecbcbcwtf/ będe strzelał w endpointy cryptohacka, w sumie chyba o to im chodziło

def decrypt(ciphertext):
    # Do decryptcji użyty jest mode ECB
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    url += ciphertext.hex()
    url += "/"
    r = requests.get(url)
    derulo = r.json()
    return bytes.fromhex(derulo["plaintext"])

def encrypt_flag():
    # encrypcji użyty jest mode CBC
    url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    r = requests.get(url)
    derulo = r.json()
    return bytes.fromhex(derulo["ciphertext"])


encrypted_flag = encrypt_flag()
print(encrypted_flag) # To jest zaszyfrowana flaga, wiemy ze do jej wytworzenia użyto tryby CBC
print(len(encrypted_flag)) # To co dostaliśmy ma 48bitów, czyli 3 blok 16 bajtów, czyli trzy macierze 4x4bytes
# Najpierw był plaintext (to czego szukamy)
# Jego pierwszy blok (nazwijmy plaintext1) został zxorowany z IV (Initialization Vector)
# Następnie to zostało zaszyfrowane w pierwszy blok ----> block1 =  encrypt(XOR(plaintext1, IV))
# Następnie drugi blok plaintext oraz block1 został zxorowany, aby zostać zaszyfrowane i stworzyć block2 ---> block2 = encrypt(XOR(plaintex2, block1))
# Tak samo trzeci blok plaintext został zxorowany z block2 i dopiero zaszyfrowany tworząc block3 ----> block3 = encrypt(XOR(plaintext3, block2))
# Tak więc aby dostać każdy plaintext i złożyc go do kupy musimy obliczyć:
# plaintext1 ^ IV = decrypt(block1) ---> plaintext1 = decrypt(block1) ^ IV
# plaintext2 ^ block1 = decrypt(block2) ---> plaintext2 = decrypt(block2) ^ block1
# plaintext3 ^ block2 = decrypt(block3) ---> plaintext2 = decrypt(block3) ^ block2
# I na koniec dodać to do siebie
def xor(a, b):
	return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

# Tu na dole mam kod, który to robi
iv = encrypted_flag[:16]
block1 = encrypted_flag[16:32]
block2 = encrypted_flag[32:]

decrypt_block1 = xor(decrypt(block1), iv)
decrypt_block2 = xor(decrypt(block2), block1)
print(decrypt_block1 + decrypt_block2)