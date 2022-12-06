import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

# co robi kod za tym endpointem?
# jest klasa StepUpCounter, którą inicjujemy jakimś value (po którym kroczymy), step (określa wielkość kroku) i step_up (bool który mowi czy step do góry jest czy w dół)
# ma ona metode increment, która idzie zmienia value o step w określoną stronę (w dół) ale to value tak jakby się przesuwa czyli jak jest 8 to to zamieniane jest na hex
# i dodawane do tego coś, ale potem value jest brane od 2 miejsca value = value[2:len(value)]

# no i potem tworzony jest cipher typu ECB (czyli każdy blok niezależnie plaintext wchodzi w AES z kluczem i wychodzi ciphertext)
# tworzony jest obiekt klasy StepUpCounter nazwany counter i pusta lista out = [] do której wpiszemy ciphertext w bajtach
# potem kod otiwera jakiś obraz png zapisany na serwerze i w pętli bierze po kolei bloki 16bajtowe
# dla każdego bloku:
    # counter jest inkrementowany
    # tworzony jest keystream jako AES wartości counter'a
    # następnie keystream bit po bicie jest xorowany z blokiem 
    # następnie to co wyjdzie jest dodawane do out
def encrypt():
    url = "http://aes.cryptohack.org/bean_counter/encrypt/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["encrypted"])

def xor(a, b):
    xored = b""
    for i in range(len(a)):
        xored += (a[i] ^ b[i]).to_bytes(1, byteorder = "big")

    return xored


# Jak to rozwiążemy? Zauważ jak powstaje pierwszy blok CTR, otóż plaintextem jest tam pierwsze 16 bajtów pliku PNG
# więc my weźmiemy pierwsze 16 bajtów encrypted i robiąc xor z jakimikolwiek innymi 16 bajtami pliku PNG dostaniemy klucz
# domyślam się, że flaga będzie obrazkiem a nie ukryta w bitach hex plaintextu obrazka z sewera 
# jak już znamy klucz to wystarczy tylko xorować po kolei z nim wszsystkie bloki zaszyfrowanego obrazka, zeby tworzyć nasz obrazek
# na koniec powstanie nam obrazek i z niego przepiszemy flagę
f = open("img/1.png", 'rb') #Tu trzeba otworzyć jakikolwiek obrazek PNG, żeby wziąć header PNG
start = f.read(16)

encrypted = encrypt()

key = xor(start, encrypted[:16])

f.close()

f1 = open("bean_flag.png", 'wb')

rnd = len(encrypted) // 16

for i in range(rnd):
    f1.write(xor(key, encrypted[i * 16: (i + 1) * 16]))

f1.close()