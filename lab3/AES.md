# How AES work



Stream ciphers - szyfrują bit po bicie XOR'ując go z kluczem

Block ciphers - szyfrują bloku po bloku (blok to może być np. 128bitów (AES-128 tak ma))

> Block ciphers only specify how to encrypt and decrypt individual blocks, and a [mode of operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation) must be used to apply the cipher to longer messages. This is the point where real world implementations often fail spectacularly, since developers do not understand the subtle implications of using particular modes. 

### Keyed permutation

![](img/1.png)

AES, like all good block ciphers, performs a "keyed permutation".  

This means that it maps every possible input block to a unique output block, with a key determining which permutation to perform.

Czyli AES dostaje blok, a klucz mu mówi jak zpermutować ten blok, to co wypluwa AES to zpermutowany blok.

Using the same key, the permutation can be performed in reverse, mapping the output block back to the original input block. It is important that there is a one-to-one correspondence between input and output blocks, otherwise we wouldn't be able to rely on the ciphertext to decrypt back to the same plaintext we started with.

![](img/2.png)

### Resisting bruteforce

If a block cipher is secure, there should be no way for an attacker to distinguish the output of AES from a [random permutation](https://en.wikipedia.org/wiki/Pseudorandom_permutation) of bits.

Output z AES czyli spermutowany blok powinien totalnie wyglądać jak coś losowego.

Furthermore, there should be no better way to undo the permutation than simply bruteforcing every possible key.

Szyf uważamy za "akademicko złamany", jeśli istnieje technika, która ma chociaż parę steps mniej niż bruteforce.

>  How difficult is it to bruteforce a 128-bit keyspace? [Somebody estimated](https://crypto.stackexchange.com/a/48669) that if you turned the power of the entire Bitcoin mining network against an AES-128 key, it would take over a hundred times the age of the universe to crack the key.



Okazuje się, że istnieje właśnie taki atak na AES, obniża on security level z 128bitów na 126.1bitów i nie został improved od 8 lat, więc luz. 

Ten atak się nazywa **Biclique attack**



> Finally, while quantum computers have the potential to completely break popular public-key cryptosystems like RSA via [Shor's algorithm](https://en.wikipedia.org/wiki/Shor's_algorithm), they are thought to only cut in half the security level of symmetric cryptosystems via [Grover's algorithm](https://en.wikipedia.org/wiki/Grover's_algorithm). This is one reason why people recommend using AES-256, despite it being less performant, as it would still provide a very adequate 128 bits of security in a quantum future.

### Structure of AES

To achieve a keyed permutation that is infeasible to invert without the key, AES applies a large number of ad-hoc mixing operations on the input.

Unlike the RSA which are based on individual math problems. AES is much less elegant, but it's very fast.



128bitowy blok, który chcemy zaszyfrować jest reprezentowany jako macierz bajtów o rozmiarze 4x4 - nazywamy ją `state`.  Algorytm ma 10 rund i w każdej rundzie `state` is modified by a number of invertible transformations. Jest kilka transformation steps and each has a defined purpose based on theoretical properties of secure ciphers established by Claude Shannon in the 1940s.

Algorytm:

1. **Key expansion / Key Schedule**
   1. Z 128bitowego klucza wydziel 11 128-bitowych `round keys` (kluczy rundowych).  
2. **Initial key addition**
   1. *AddRoundKey* - the bytes of the first round key are XOR'd with the bytes of the state. Czyli XOR pierwszego` round key` z `state`
3. **Round** - this phase is looped 10 times, 9 main round and 1 final
   1. ***SubBytes*** - each byte of the state is substituted for a different byte according to a lookup table ("S-box"). 
      1. Czyli jest jakaś tablica S-box, która mówi ja podmieniać bajty - całe bajty całe 8 bitów jest jakoś mapowane.
   2. ***ShiftRows*** - the last three rows of the state matrix are transported —shifted over a column or two or three.
      1. Pierwszy bajt z drugiego wiersza przenosimy na ostatnią kolumnę (ale nie zamieniamy, robimy shift)
      2. W trzecim wierszu dwa bajty
      3. W czwartym wierszu trzy bajty
   3. ***MixColumns***  - matrix multiplication is performed on the columns of the state, combining the four bytes in each column. This is skipped in the final round.
   4. ***AddRoundKey***  -  the bytes of the current round key are XOR'd with the bytes of the state.

[Ten filmik uczy fest](https://www.youtube.com/watch?v=gP4PqVGudtg)

