import math

def calculate_vector_multiplication_value(vector1, vector2):
    start = 0
    for i in range(4):
        start += vector1[i] * vector2[i]

    return start

v = [0] * 4
#wektory z zadania
v[0] = [4, 1, 3, -1]
v[1] = [2, 1, -3, 4]
v[2] = [1, 0, -2, 7]
v[3] = [6, 2, 9, -5]

#significant figures 5
for i in range(4):
    for j in range(i): #chcemy dojsc do u4 zgodnie z poleceniem
        inner = calculate_vector_multiplication_value(v[i], v[j]) # obliczamy vi*uj
        size = calculate_vector_multiplication_value(v[j], v[j]) # obliczamy ||uj||^2
        mi = inner / size # obliczamy zadany iloraz inner/size
        # zarowno mi jak i koncowe ui iterujemy po 1<=j<i przez co wkladamy to do jednej petli
        
        for k in range(4):
            v[i][k] -= v[j][k]  * mi

print(v[3][1])