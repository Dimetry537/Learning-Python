<<<<<<< HEAD
# написать единичную матрицу с использованием циклов for
=======
x = [0 for i in range(16)]
n = 4
y = [x[i:i+n] for i in range(0,16,n)]
z = [[1 if m == n else 0 for m, _ in enumerate(y[n])] for n, _ in enumerate(y)]

for i in z: print(i)
>>>>>>> b24fdb0 (make an identity matrix)
