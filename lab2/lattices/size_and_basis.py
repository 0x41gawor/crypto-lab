def v_dot(v1, v2):
    res = 0
    for i in range(3):
        res += v1[i] * v2[i]
    return res
v = [4, 6, 2, 5]

print(v_dot(v,v))