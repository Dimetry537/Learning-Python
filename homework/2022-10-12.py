# задача возвести все элементы в квадрат через функцию map 
array = [1, 3, 4, 6, 10]

def add_10(element):
    return element + 10

print(add_10(10))

print(list(map(add_10, array)))

array = [1, 3, 4, 6, 10]

def square(element):
    return element * element

print(add_10)

add_10 = lambda elem : elem + 10

print(add_10)

print(list(map(lambda elem : elem * elem, map(lambda elem : elem + 10, array))))

print(list(filter(lambda elem : elem  % 2 == 0, array)))