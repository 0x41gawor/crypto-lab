import numpy

v1 = [6, 2, -3]
v2 = [5, 1, 4]
v3 = [2, 7, 1]

matrix = numpy.array([v1,v2,v3])
det = numpy.linalg.det(matrix)
print(abs(det))