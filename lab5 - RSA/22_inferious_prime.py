# Opis kodu szyfrującego w readme.md

N = 742449129124467073921545687640895127535705902454369756401331
e = 3
ciphertext = 39207274348578481322317340648475596807303160111338236677373

# zeby dostać plaintext (a w nim flagę) to muszę zrobić `pow(ciphertext, d, N)`
# skąd wziąć `d` w takim razie? 
# do to się równa pow(e, -1, totient)
# skąd wziąć totient?
# totient to jest (p-1)*(q-1)
# skąd wziąć `p` i `q`?
# z dupy 
# nie no zart w poprzednim zadaniu nauczyliśmy się rozbijać `N` na `p` i `q`  # okazuje sie ze nie taki zart bo nie mozna korzystać z factordb
# jak mam zainstalowane factordb to zrobię po prostu w terminalu 
# factordb 742449129124467073921545687640895127535705902454369756401331

p = 752708788837165590355094155871
q = 986369682585281993933185289261

totient = (p-1)*(q-1)

d = pow(e, -1, totient) # klucz prywatny mam :D

plaintext = pow(ciphertext, d, N) # plaintext odszyfrowany ale to long

from Crypto.Util.number import long_to_bytes
byted_from_longed_xd_plaintext = long_to_bytes(plaintext)
print(byted_from_longed_xd_plaintext)