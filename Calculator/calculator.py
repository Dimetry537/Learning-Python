from Stack.stack import Stack

class Calculator:
    PRIORITIES = {
        '*': 2,
        '/': 2,
        "+": 1,
        "-": 1
    }
    def __init__(self, exprasion):
        self.exprasion = exprasion

    def reverse_polish_notation(self):
        pass
        ## return 2 2 * 2 +

    def calculate(self):
        pass
        ### 6



# 2+2*2

# (8 + 10) * (2 + 2)
# 8, 10 + 2, 2 + *

# (2 + 2 * 2) / (2 + 2 * 2)


# 6 / 2 * (1 + 2)

# result: 6 2 / 1 2 + *
# stack:  

# 3 - 2

# 3 + (-2)

# группоид
# хуй  пизда джигурда + 
# хуй + пизда = джигурда

# группа

# (a + b) + c = a + (b + c) - ассоциативность
# а + 0 = а - есть нейтральный элемент
# a + (-a) = 0 - противожный

# абелева группа
# а + b = b + a

# (a * b) * c = a* (b * c)
# a * 1 = a
# a * (1/a) = 1
# a * b = b * a

# область целостности - нету комутотивности по умножени

# поле (+, *)

# алебева группа по сложению и умножения


# https://en.wikipedia.org/wiki/IEEE_754


