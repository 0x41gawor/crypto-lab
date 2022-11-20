with open("input.txt", "r") as f:
    input = eval(f.read())

from Crypto.Util.number import long_to_bytes

# p sobie podejrzałem 
p = 1007621497415251

res = ""
for b in input:
    # Jeżeli to co teraz rozpatrujemy jest Quadratic Reside pierścienia p to tam wpisano 1 
    legendre = pow(b, (p-1)//2, p)
    if legendre == 1:
        res += "1"
    else:
        # a jeśli nie to 0
        res += "0"

print(long_to_bytes(int(res, 2)))