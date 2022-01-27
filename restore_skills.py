import array
import time
from math import floor, ceil
# вывести на экран строку "Привет"

# print('привет')

# программа приветствия пользователя
# user enter the name, program write on the screen - Hello, %username%!
# print('Enter your name')
# name = input()
# print('Hello, ' + name + '!')

# Program which will say Hello, mr(ms) %username
# User enter sex and name
# if User enter into sex something not like man or woman program prints nothing
# print('Enter your name')
# name = input()
# print('Enter your sex')
# sex = input()
# if sex == 'man':
#     into_sex = 'mr.'
# elif sex == 'woman':
#     into_sex = 'ms.'
# else:
#     exit()
# print('Hello, ' + into_sex + name + '!')

# print sum of array
# array = [1,1,1,1,1]
# sum = 0
# for x in array:
#     sum = sum + x
# print(sum)

# print biggest element in array (max)
# array = [-2, -3, -1000500 , -40000000, -1, -5, -6]
# max_value = array[0]
# for x in array:
#     if max_value < x: # x = 2, max_value = 0, 0 > 2 == False
#         max_value = x
# print(max_value)

# proram prints geometric progression
# user enter number of element, base and step
# base = 2, step = 2, number = 3, 2,4,8
# program prints numbers till that number
# print('Enter base number')
# base = int(input())
# print('step')
# step = int(input())
# print('length')
# length = int(input())
# - an = base * step ** (n-1)
# + an = an-1 * step
# #geometry = base - 1 * step
# #an = base
# for geometry in range (1, length + 1):
#     base = base * step
#     print(base)
# print(base)



# print result of factorial 5! = 1*2*3*4*5 = 120
# user enter the number 
# code prints factorial
# print('Enter factorial number')
# factorial = int(input())
# number = 1
# for x in range(1, factorial+1):
#     number = number*x
# print(number)


#1. наисать программу которая выведет все числа которые делятся нацело на 5
# array = [1,3, 5, 10, 21, 3, 12, 5, 15]

# x = 5

# for x in array:
#     if x %5 == 0:
#         print(x)

#2. реализовать бинарный поиск по массиву
# пользователь вводит искомое число
#array = [1,2.5,3,4,6,7,8,9]
# 1036
# 3848

# (3848 + 1036)/2 = 2442

# (3848 - 1036)/2 + 1036 = 2442

# середина = (КЗ + НЗ)/2  

n = 100000000
array = array.array('i',(i for i in range(0,n)))



print('Enter your number')
number = float(input())

start_time = time.perf_counter ()
for i in array:
    if i == number:
        print('found')
end_time = time.perf_counter ()
print(end_time - start_time, "seconds")


start_time = time.perf_counter ()
start = 0
end = len(array) - 1
middle = floor((end + start)/2)
 
while True: 
    middle_value = array[middle]
    if middle_value == number:# ISO 754
        print('found')
        break
    if middle_value > number:
        end = middle
        middle = floor((end + start)/2)
    if middle_value < number:
        start = middle
        middle = ceil((end + start)/2)
    if end == start:
        print('value is not found')
        break
end_time = time.perf_counter ()
print(end_time - start_time, "seconds")

# почитать структуру данных стек и написать класс ее реализации (в отдельной папке strcutures)
# class Stack:
#   def __init__
#   def push
#   def pop
# почитать обратную польскую нотацию и алгоритм преобразования в нее и вычисления по ней
# 


# print all numbers which devided by 4 with no остатка

# for i in array:
#     if i % 4 == 0:
#         print(i)


# print sum of all numbers divided by 10

from array import array


array_witt_10 = [1, 20, 20, 3, 4, 2, 7, 10, 20, 30]

# for i in array_witt_10:
#     if i % 10 == 0:
#         print(i)

# 1232 + 321 + 2351 + 4233

# 0    + 1232 = 1232
# 1232 + 321 = 1553
# 1553 + 2351 = 3904
# 3904 + 4233 = 8137

# k = 0

# for i in array_witt_10:
#     if i % 10 == 0:
#         k = k + i
# print(k)



array_uvasa = [231,   123,   1231, 1237321]
array_lesha = [68731, 21312, 314,  12313]
# 231 + 68731 = array_uvasa[0] + array_lesha[0] = array_sum[0]
# 123 + 21312 = array_uvasa[1] + array_lesha[1] = array_sum[1]
# 1231 + 314 = array_uvasa[2] + array_lesha[2] = array_sum[2]
# 1237321 + 12313 = array_uvasa[3] + array_lesha[3] = array_sum[3]

# [0,0]

# array = []
# array.append(4)
# array -> [4]
# array.append(4)
# arrya -> [4, 4]
# array.append(4)
# array -> [4, 4, 4]

array_sum = []

for i in range(len(array_lesha)):
    array_sum.append(0)

print(array_sum)

for i in range(len(array_lesha)):
    array_sum[i] = array_uvasa[i] + array_lesha[i]
print(array_sum)

# написать матрицу с ее введением (массив с вложенным массивом [[], [], []])

# написать программу, которая будет угадывать число