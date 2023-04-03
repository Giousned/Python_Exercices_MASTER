# Your code here
def factorial(num):

    total = 1

    for i in range(num,1,-1):
        total *= i

    return total

print(factorial(8))


# SOLUCIONES DADAS
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x=int(input())
# print (fact(x))


# OR
# import math
# def factorial(num):
#     return math.factorial(num)

# print(factorial(8))