import math

def v_dot(v1, v2):
    res = 0
    for i in range(4):
        res += v1[i] * v2[i]
    return res

v = [ [], [], [], []]
v[0] = [4, 1, 3, -1]
v[1] = [2, 1, -3, 4]
v[2] = [1, 0, -2, 7]
v[3] = [6, 2, 9, -5]


for i in range(4):
    for j in range(i): 
        inner = v_dot(v[i], v[j]) 
        size = v_dot(v[j], v[j]) 
        mi = inner / size 

        for k in range(4):
            v[i][k] -= v[j][k]  * mi

print(v[3][1])