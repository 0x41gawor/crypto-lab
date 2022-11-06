# Zamiana z ASCII na int

`chr(int)` - int na char

`ord(str) `- char na int

## hex string <-> byte string

Jak coś enkryptujemy to resulting **ciphertext** jest ciągiem bajtów (zer i jedynek). Jak chcemy to trochę zwęzić i jakoś ładniej przedstawić to możemy z bajtów zrobić hex string.	

`bytes.fromhex(hexstr)` - zamienia hexstring na byte string

`.hex()` może zostać użyta na byte string, żeby dostać hex string

## Base64

Kolejny takim jak hexstring sposobem na przedstawienie ładniej ciągu bitów jest base64. Zamienia on bajty na znaki z tablicy ASCII.

Czyli tak jak hexstring bierze 4 zera i jedynki i zamienia na jeden znak, tak base64 bierze 6 zer i jedynek i zamienia na znak ASCII.

![](img/1.png)

Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

Żeby zakodować byte string w base64 trzeba użyć `base64.b64encode(byte_str)`

Żeby z base64 zdekodować na ciąg bajtów - `base64.b64decode(base64_str)`

## XOR

o xorze powiem tyle ze xoruje się bajt po bajcie

|  A   |  B   | A^B  |
| :--: | :--: | :--: |
|  0   |  0   |  0   |
|  1   |  0   |  1   |
|  0   |  1   |  1   |
|  1   |  1   |  0   |

Zauważ własność:

```
A = 0001011
B = 1010011
A^B = 1011000 = C //nazwijmy te zmienną C
// co się okazuje to to że jak zrobimy xor B ^ C
B^C = 001011 // to wychodzi A
stąd
if A^B=C ==> A^C=B and B^C=A
```

Reszta własności:

![](img/2.png)

### Funkcja do XORowania byte strings

```python
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

key1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key2 = byte_xor(key1,bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'))
```



# Maths

Dwie liczby są **congruent modulo m**, co zapisujemy jako:

```
a -=- b mod m
```

congruent - przystające, zgodne

Co oznacza, że `a` podzielone przez `m` daje remainder `b`

np. 

```
11 -=- 5 mod 6 // 11 i 5 są zgodne co do modulo 6
44 -=- 4 mod 5 // 84 i 4 dzieli ileś wielokrotności piątki
11 -=- 5 mod 6 // 11 i 5 dzieli ileś wielokrtności (jedna) szóstki
```

Ważna zależność jest taka, że jeśli `m` dzieli bez reszty `a` to `b=0`.  

To, ze `m` dzieli bez reszty `a` zapisujemy jako `m | a`. No i wtedy ofc `a -=- 0 mod m`. Czyli `a` i `0` dzieli jakaś wielokrotność `m`.

### Pierścienie i pola

Dzielenie liczby przez modulo `p` (gdzie `p` jest stałe) definiuje pewien pierścień, oznaczany przez `Fp`.

> Np. Pierscień modulo 5, czyli F5 to są liczby {0,1,2,3,4}.
>
> Pierścień modulo 8 to {0,1,2,3,4,5,6,7}
>
> Dlaczego? Bo jak weźmiesz wszystkie liczby świata po kolei i zaczniej je modulo `p` dzielić to  Ci wyjdzie właśnie taka pętla.

Dobra, teraz ogarniczmy się tylko i wyłącznie do `p`, które jest liczbą pierwszą.

Teraz `Fp` nie jest pierścieniem tylko *Finite field*, czyli polem skończonym.

Jest to zbiór liczb {0, 1,2, p-1} oraz zdefiniowane dla niego działania dodawania i mnożenia, z zdefiniowanymi **elementami odwrotnymi** (inverse element), takimi że:

```
Dla każdego elementu `a` istnieje odwrotny `b`, taki że
a+b=0
a*b=1
czyli w działaniach daje wynik neutralny dla danego działania (wynik neutralny (identity) to takie ze a+0=a oraz a*1=1)
```

## Zadanie modular 2

Let's say we pick pole `F17`, 17 to liczba pierwsza.

Mamy obliczyć `3^17 mod 17`.

Generalnie to wiemy, że wynik będzie należał do pola F17 czyli będzie w zbiorze {0,..16}.

W zadaniu licząc ręcznie zauważamy zależność, która się nazywa Fermat Little Theoremi mówi o tym, że:

**Jeśli `p` jest liczbą pierwszą, to dla każdą liczbę `a^p` od liczby `a` dzieli ileś wielokrotności `p`. Co zapisujemy jako `a^p -=- a mod p`**.

>Np. liczby 8 i 2. 8 to 2^3, czyli p=3, no a między 8 i 2 są dokładnie dwie trójki.
>
>Kolejny przykład: p=5 , 3^5 i 3 dzieli równo 48 piątki.

 **Jeśli `p` jest liczbą pierwszą, a liczba `a` jest coprime z `p` to wtedy liczba `a^(p-1)-1` jest oddalona od `p`. **
**Co zapisujemy jako `a^(p-1) -=- 1 mod p`**. 

> Np. liczby 64 i 1 są oddalone od siebie o dziewięć wielokrotności 7. Bo da się zapisać 2^6 -=- 1 mod 7
>
> Dzięki temu jeślli np. mamy obliczyć `3^6 % 7`, to wybieramy, że nasze `p` to 7, a `a` to 3. Są one coprime. Więc da się zapisać, że 3^6 -=- mod 7. 
> Czyli wiemy, że `3^6 % 7 = 1`.

### Zadanie inverse 

`Fp` to jest closed field. Czyli ma elementy `{0, ... Fp-1}` i dodając/mnożąc nigdy nie wyjdziemy z tego zbioru.

Zdefiniujmy sobie czym jest **multiplicative inverse element** w `Fp`.

![](img/3.png)

> Na przykład dla ringu F5, który się składa z liczb {0, 1, 2, 3, 4}. Znajdźmy inverse element dla 2.
>
> 2 * d -=- 1 mod 5, czyli d = 3, bo 6 % 5 = 1

W zadaniu było W F13 znaleźć inverse dla `3`:

`3 * d -=- 1 mod 13`, czyli co modulo 13 da 1. Otóż 27, więc d = 9.

