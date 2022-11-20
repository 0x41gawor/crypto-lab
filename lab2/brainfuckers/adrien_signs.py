p= 1007621497415251 # nasz podany parametr p

# musimy znalezc power dla kazdego z elementow ciphers
binary=''
for i in ciphers:
    r=pow(i,(p-1)//2,p) # dla kazdego elementu z outputu wyliczamy legendre symbol i jesli jest on rowny jeden czyli i jest QR to rozszerzamy nasz string o 1 a jesli nie to o 0
    if r==1:
        binary+='1'
    else:
        binary+='0'
print(long_to_bytes(eval('0b' + binary))) # na sam koniec przechodzimy