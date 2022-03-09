import array
#  на продолжение циклов: написать програаму вычисления растояний между веторам (списками)

vector_a = [1,2,2,3,3,4,4,5]
vector_b = [2,3,4,4,5,5,6,7]
# sqrt(1*2 + 2*3 +...)
# сколярное произведение

# vector_a[1] * vector_b[1] + vector_a [2] * vector_b[2]....

# vector_c = []

# for i in range(len(vector_a)):
    
#     vector_c.append(0)

#     vector_c[i] = vector_a[i] * vector_b[i]

k = 0

for i in range(len(vector_a)):
    k = vector_a[i] * vector_b[i]
    b = sum(k[i])
    print(b)