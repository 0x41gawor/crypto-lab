# https://stackoverflow.com/questions/12826114/euclids-extended-algorithm-c
def xgcd(a,b): 
    x = int(0)
    y = int(1)
    lastx = int(1)
    lasty = int(0)

    while(b!= 0):
        q = int(a/b)
        temp1 = a%b
        a = int(b)
        b = int(temp1)

        temp2 = x
        x = lastx - q*x
        lastx = temp2

        temp3 = y
        y = lasty - q*y
        lasty = temp3
    return lastx, lasty

print(xgcd(26513,32321))