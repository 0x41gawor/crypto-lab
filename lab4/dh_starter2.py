p = 28151

# order - liczba elementów pierścienia
def order_of_element(g):
    # przechodzimy przez wszystkie potęgi g: g^1, g^2, g^3, ... czyli tworzymy kolejne elementy subgroup'y
    for n in range(2, p):
        # jesli znowu jakis element z subgropy jest równy tyle co g^1, to wtedy niemożliwe ze order `g` jest równy orderowi `p`(bo mamy powtórkę)
        if pow(g, n, p) == g:
            return n
    # jeśli nie znalazło się nic takiego to order g (czyli liczba elementów jego subgroup'y) jest równy orderowi Fp czyli `p`
    return p

for g in range(p):
    order = order_of_element(g)
    # dla pierwszego elementu Fp, którego order jest równy p przerywamy pętle
    if order == p:
        print(g)
        break