from random import randint

a = 288260533169915  # duza liczba nwm czy pierwsza
p = 1007621497415251 # bardzo duza liczba pierwsza

FLAG = b'crypto{????????????????????}' 


def encrypt_flag(flag):
    ciphertext = [] # na poczatku lista puste
    # plaintext to string który ma bajty, zrobione tak ze kazdy znak z FLAG zostal zamieniony na binarny odpowiedni fcją `bin` i dopełniony zerami fcją `zfill(8)` 8-bo do pełnego bajta
    # czyli kazdy znak to plain jego bajt binary
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    # iterujemy po kazdym bajcie z plaintextu
    for b in plaintext:
        # losujemy jakas liczba exponent miedzy 1 a p
        e = randint(1, p)
        # n to a^e % p,
        n = pow(a, e, p)
        # jeśli current bit jest 1, to do ciphertext dajemy `n`
        if b == '1':
            ciphertext.append(n)
        else:
            # jeśli 0 to (-n) modulo p
            n = -n % p
            ciphertext.append(n)
    return ciphertext


encrypt_flag(FLAG)
