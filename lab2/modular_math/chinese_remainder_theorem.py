x = 0 # nasza duza liczba `x`
# i to kandydaci na `x`
for i in range(935):
    # szukam takiego duzego `x` zeby spelnial wszystkie przystawania (conguerencje)
	if i % 5 == 2 and i % 11 == 3 and i % 17 == 5:
		x = i
# W zadaniu trzeba znaleźć `a` a nie `x`, więc korzysta ze wzory `x % N = a`
print(x%935)

