# N = p * q
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
# public key = N, e
e = 65537

# d to jest multiplicative inverser of `e` modulo the totient of `N`
totient = (p-1)*(q-1)

# d = e^-1 (mod Totient) ====> e*e^-1 === 1 (mod Totient)
d = pow(e, -1, totient)

# skoro ciphertext = pow(message, e, N)
# to plaintext = pow(ciphertext, d, N)
c = 77578995801157823671636298847186723593814843845525223303932

N = p*q
print(pow(c,d,N))