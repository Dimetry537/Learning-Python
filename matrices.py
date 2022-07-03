matrix_size = int(input("Введите размер квадратной матрицы: "))

#matrix_input_1 = input("Введите элементы маирицы #1 через пробел: ")
#matrix_input_2 = input("Введите элементы маирицы #2 через пробел: ")

matrix_1 = list(map(int,input("Введите элементы маирицы #1 через пробел: ").split()))

print(matrix_1)

first_matrix = []

for i in range(matrix_size):
    first_matrix.append(matrix_1)
    
print(first_matrix)