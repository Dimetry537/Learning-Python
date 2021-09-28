# написать единичную матрицу с использованием циклов for
#matrix = input('Ensert data of identity matrix')

''' [1 0 0 0 0]
    [0 1 0 0 0]
    [0 0 1 0 0] 
    [0 0 0 1 0]
    [0 0 0 0 1]'''
'''test_identity_matrix = str([1, 0, 0, 0]), str([0, 1, 0, 0]), str([0, 0, 1, 0]), str([0, 0, 0, 1])

for x in test_identity_matrix:
    for i in x:
    x = row(test_identity_matrix)

print(x)
'''
'''def identity_matrix(n):
    m=[[0 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        m[i][i] = 1
    return m

m = identity_matrix(6)
print(m)
'''
units = 1
zeroes = 0

for x in zeroes:
    for y in units:
        
    print (x)