def inner_product(a, b):
	ans = 0
	for i in range(2):
		ans += a[i] * b[i]

	return ans

def v_subtract(v1, v2):
    res = [0, 0]
    for i in range(2):
        res[i] = v1[i] - v2[i]
    return res

def v_dot(v1, v2):
    res = 0
    for i in range(2):
        res += v1[i] * v2[i]
    return res

def gauss(v1, v2):
	# a)
	if v_dot(v1, v1) > v_dot(v2, v2):
		return gauss(v2, v1)
	# b)
	m = v_dot(v1, v2) // v_dot(v1, v1)
	# c)
	if m == 0:
		return v1, v2
	# d)
	v2 = v_subtract(v2,v1)

	return gauss(v1, v2)

v = [846835985, 9834798552]
u = [87502093, 123094980]

u, v = gauss(u, v)
print(v_dot(u, v))