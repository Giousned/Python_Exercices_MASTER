#Complete the function to return the tens digit and the ones digit of any interger.
import math

def two_digits(digit):

  decenas = int(digit/10)

  unidades = digit % 10

  return decenas, unidades
   


#Invoke the function with any interger as its argument.
print(two_digits(79))


# OTRA SOLUCION
# def two_digits(digit):

#   decenas = math.trunc(digit/10)

#   unidades = digit % 10

#   return decenas, unidades

# OTRA SOLUCION
# def two_digits(digit):

#   decenas = math.floor(digit/10)

#   unidades = digit % 10

#   return decenas, unidades