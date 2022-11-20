import numpy 

def gaussian_reduction(v1, v2):
    while(True):
        # a)
        if v2.size < v1.size:
            v1, v2 = v2, v1
        print(f"v1: {v1}")
        print(f"v2: {v2}")
        # b)
        m = numpy.dot(v1,v2) // numpy.dot(v1,v1)
        print(f"m: {m}")
        # c)
        if m == 0: 
            return (v1,v2)
        # d)
        numpy.subtract(v2,m*v1)

v = numpy.array([846835985,9834798552])
u = numpy.array([87502093,123094980])

r1, r2 = gaussian_reduction(v,u)
print(f"r1: {r1}, r2: {r2}")
print(numpy.dot(r1,r2))
v2 = numpy.array([5,5])
v1 = numpy.array([1,1])

print(numpy.subtract(v2,5*v1))


