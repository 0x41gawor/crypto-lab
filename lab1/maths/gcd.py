# https://www.matemaks.pl/algorytm-euklidesa.html
a = 66528 # a musi byc wieksze !!!
b = 52920

h = a # wieksza liczba
l = b # mniejsa liczba
while(True):
    remainder = h % l
    if remainder == 0:
        result = l
        break
    h = l
    l = remainder

print(result)
