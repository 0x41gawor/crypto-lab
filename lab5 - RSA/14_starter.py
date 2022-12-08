# N = p * q
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
# public key = N, e
e = 65537

# d to jest multiplicative inverser of `e` modulo the totient of `N`
totient = (p-1)*(q-1)

# d = e^-1 (mod Totient) ====> e*e^-1 === 1 (mod Totient)
d = pow(e, -1, totient)
print(d)