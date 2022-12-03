from Crypto.Cipher import AES
import hashlib




def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted


# Otwieram plik words, link do pliku był w zadaniu
with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

# Lece po wszystkich słowach z tego pliku, może akurat hash jakiegoś z tych słów jest kluczem
for i in range(len(words)):
    KEY = hashlib.md5(words[i].encode()).digest()
    # to dostaje jak klikne ENCRYPT_FLAG() pod linkiem http://aes.cryptohack.org/passwords_as_keys/
    encrypted_flag_ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
    plaintext = decrypt(encrypted_flag_ciphertext, KEY)

    if plaintext[0] == ord('c') and plaintext[1] == ord('r'):
        print(plaintext.decode())