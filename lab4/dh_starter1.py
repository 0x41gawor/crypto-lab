from Crypto.Util.number import inverse

p = 991 # modulo field'a p w notacji `Fp`
g = 209 # element pola, którego inverse szukamy

print(inverse(g, p))

