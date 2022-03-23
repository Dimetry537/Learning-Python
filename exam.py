# начальное значение - 100
# конечное значение - 32
# шаг цикла - -50
# счетчик цикла - k - однозначное определяет итерацию

# Присваиваем начальное значение к счетчику цикла
# Пока счетчик цикла не достиг конечного значение
#     исполняем цикл
#     Мееняем счетчик чикла на шаг цикла

k = 1
while k < 10:
    g = 1
    while g < 10:
        print (g * k, end='\t')
        g += 1
    print("")
    k += 1


print("")
i = 5
for g in range(1, 10):
    print (g * i, end='\t')

print("")

for i in range(1, 10):
    for g in range(1, 10):
        print (g * i, end='\t')
    print("")

matrix = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]

for i in range(len(matrix)):
    print("{", end="")
    for j in range(len(matrix[i])):
        if j == len(matrix[i]) - 1:
            print(matrix[i][j], end='')
        else:
            print(matrix[i][j], end=',') 
    print("}")

print("")
# Присваиваем начальное значение к счетчику цикла
# Пока счетчик цикла не достиг конечного значение
#     исполняем цикл
#     Мееняем счетчик чикла на шаг цикла

i = 0

while i < len(matrix):
    print("{", end="")
    j = 0
    while j < len(matrix[i]):
        if j == len(matrix[i]) - 1:
            print(matrix[i][j], end='')
        else:
            print(matrix[i][j], end=',')
        j += 1
    print("}")
    i += 1