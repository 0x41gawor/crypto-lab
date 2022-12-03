# Intro

The Diffie-Hellman key exchange (DH) is central to the security of the internet today. As part of the TLS handshake, it's typically used to securely compute a shared AES encryption key over the internet between a web browser and server.

DH relies on the assumption that the discrete logarithm problem (DLP) is difficult to solve. 

## Diffie-Hellman starter 1

**ring**

The set of integers modulo `n`, together with the operations of both addition and multiplication is a ring. This means that adding or multiplying any two elements in the set returns another element in the set.

**field**

When the modulus is prime: `n = p`, we are guaranteed an inverse of every element in the set, and so the ring is promoted to a field. We refer to this field as a finite field `Fp`.

**Zadanie**

Given the prime `p = 991`, and the element `g = 209`, find the inverse element `d` such that `g * d mod 991 = 1`

**Solve**

W pythonie do takich rzeczy jest funkcja `inverse`

