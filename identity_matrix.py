# написать единичную матрицу с использованием циклов for
#matrix = input('Ensert data of identity matrix')
#прибавление матриц по индексу две единичные матрицы каждый индекс к каждому индексу другой матрицы

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
# def identity_matrix(n):
#     m=[[0 for x in range(n)] for y in range(n)]
#     for i in range(0, n):
#         m[i][i] = 1
#     return m

# print(identity_matrix(6))

# TODO make this to work on code
# [1 1 1]    [1 1 2]     [2 2 3]
# [1 1 1] +  [1 2 1]  =  [2 3 2]
# [1 1 1]    [2 1 1]     [3 2 2]

# [1 1 1]    [1 2 2]     [1*1 + 1*1 + 1*2 1*2 + 1*2 + 1*1 1*2 + 1*1 + 1*1]     [4 5 4]
# [1 1 1] *  [1 2 1]  =  [1*1 + 1*1 + 1*2 1*2 + 1*2 + 1*1 1*2 + 1*1 + 1*1] =   [4 5 4]
# [1 1 1]    [2 1 1]     [1*1 + 1*1 + 1*2 1*2 + 1*2 + 1*1 1*2 + 1*1 + 1*1]     [4 5 4]

# [1 0 0]    [1 2 2]     [? ? ?]     [1 2 2]
# [0 1 0] +  [1 2 1]  =  [? ? ?] =   [1 2 1]
# [0 0 1]    [2 1 1]     [? ? ?]     [2 1 1]

# def funct_check(test, test_2, test_3, test_4, test_5, test6):
#     print(test, test_2, test_3, test_4, test_5, test6)

# x * y = 0 => x = 0 OR y = 0

# funct_check(1,2,3,4,5,6)

# funct_check(1,0,0,0,5,0)

# funct_check(1,5,6,8,9)


# x * y = 0

# 2 * 0 = 0
# 2 * 0 = 5 * 0
# 2 = 5

# 2 + 2 = 4

# 2 + 2  = 4 + 5 * 0
# 2 + 2 + (2 + 2)  * 0 = 4 + 5 * 0
# 4 + (2 + 2 )* 0 - 4 = 5 * 0
# (2 + 2 ) * 0 = 5 * 0
# 2 + 2 = 5


# x*e = x
# x * y = e => y обратный элемент к x e/x

# абелева группа
# a + (b + c) = (a + b) + c - ассоциативность
# x + (-x) = 0 - противоположные элементы
# 0 - нулевой элемент
# a + b = b + a - коммутативность



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
unit = 1
n = 20
zero = 0

# matrix = [zeroes] * n

# for x in range(n):
#     # matrix = [zeroes] * n
#     matrix[x] = unit
#     for y in range(x):
#        matrix[y] = zero
#     print(matrix)


for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print('')


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