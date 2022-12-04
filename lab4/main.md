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

## Diffie-Hellman starter 2

**Subgroup**

Every element of a finite field `Fp` can be used to make a subgroup `H` under repeated action of multiplication. 

In other words, for an element `g` jego subgroup to  `H = {g, g^2, g^3, ...}`

**Primitive**

A **primitive** element of `Fp` is an element whose subgroup `H = Fp`

*i.e.*, every element of `Fp`, can be written as `g^n mod p` for some integer `n`

Because of this, primitive elements are sometimes called **generators** of the finite field.

**Zadanie**

For the finite field with `p = 28151` find the smallest element `g` which is a primitive element of `Fp`.

**Solve**

W kodzie

## Diffie-Hellmans tarter 3

The Diffie-Hellman protocol is used because the discrete logarithm is assumed to be a "hard" computation for carefully chosen groups.



- The first step of the protocol is to establish a prime `p` and some generator of the finite field `g`

  - > These must be carefully chosen to avoid special cases where the discrete log can be solved with efficient algorithms. For example, a safe prime `p = 2*q +1` is usually picked such that the only factors of `p - 1` are `{2,q}` where `q` is some other large prime. This protects DH from the [Pohlig–Hellman algorithm](https://en.wikipedia.org/wiki/Pohlig–Hellman_algorithm).

- The user then picks a secret integer `a < p` and calculates `g^a mod p`.

  - >  This can be transmitted over an insecure network and due to the assumed diffculty of the discrete logarithm, if the protocol has been implemented correctly the secret integer should be infeasible to compute.

## Diffie-Hellmans tarter 4

W kodzie

## Diffie-Hellmans tarter 5

Tutaj jest tak jak w poprzednim zadaniu, z tym, że to co sobie przesłaliśmy to nasz `shared_key` do algorytmu AES, którego teraz używamy w komunikacji (między innymi Alice nam wysyłała flagę :happy:)

