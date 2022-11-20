def inner_product(a, b):
	ans = 0
	for i in range(2):
		ans += a[i] * b[i]

	return ans

def gauss(a, b):
	if inner_product(a, a) > inner_product(b, b):
		return gauss(b, a)

	m = inner_product(a, b) // inner_product(a, a)

	if m == 0:
		return a, b

	for i in range(2):
		b[i] -= m * a[i]

	return gauss(a, b)

v = [846835985, 9834798552]
u = [87502093, 123094980]

(u, v) = gauss(u, v)
print(inner_product(u, v))