v = [2,6,3]
w = [1, 0, 0]
u = [7, 7, 2]

def v_subtract(v1, v2):
    res = [0, 0, 0]
    for i in range(3):
        res[i] = v1[i] - v2[i]
    return res

def v_add(v1, v2):
    res = [0, 0, 0]
    for i in range(3):
        res[i] = v1[i] + v2[i]
    return res

def v_dot(v1, v2):
    res = 0
    for i in range(3):
        res += v1[i] * v2[i]
    return res

def vs_multiply(scalar, vector):
    res = [0, 0, 0]
    for i in range(3):
        res[i] = scalar * vector[i]
    return res

print( v_dot( vs_multiply(3,v_subtract(vs_multiply(2,v),w)), vs_multiply(3,u)  ) )