# написать единичную матрицу с использованием циклов for
#matrix = input('Ensert data of identity matrix')

''' [1 0 0 0 0]
    [0 1 0 0 0]
    [0 0 1 0 0] 
    [0 0 0 1 0]
    [0 0 0 0 1]'''
'''test_identity_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

for x in test_identity_matrix:
    for i in x:
    x = row(test_identity_matrix)

print(x)
'''
# def identity_matrix(n, m, p, i, m, t, o, a, p, 4):
#     m=[[0 for x in range(n)] for y in range(n)]
#     for i in range(0, n):
#         m[i][i] = 1
#     return m

# m = identity_matrix(6)
# print(m)


# def funct_check(test, test_2, test_3, test_4, test_5, test6):
#     print(test, test_2, test_3, test_4, test_5, test6)

# funct_check(1,2,3,4,5,6)

# funct_check(1,0,0,0,5,0)

# funct_check(1,5,6,8,9)

# units = 1
# zeroes = 0

# for x in zeroes:
#     for y in units:      
#        print(x)


#list = [12 , 500]

#print(list)

# for x in list:
#     print(list)
#     print(x)

# for x in list:
#     print("x =", x)
#     for y in list:
#         print("y =", y)
#         print(list)

zeroes = 0 #' 0 '
units = 1
n = 10
z = 0

matrix = [zeroes] * n

for x in range(n + 2):
    print(matrix)

# a0 = 0
# n = 10
# d = 5

# an = a0
# sum = 0
# for i in range(n):
#     sum += an
#     an += d

# print("sum is ", sum)
# print("sum check is ", (a0 + d*(n-1))*n/2)

# for x in range(10):
#     zeroes_all = zeroes_start + zeroes + zeroes_end

# print(zeroes_all)

# for x in range(4):
#     print(zeroes)

# En+1 = En + D
# En+1 = En * D
# En+1 = En ** D