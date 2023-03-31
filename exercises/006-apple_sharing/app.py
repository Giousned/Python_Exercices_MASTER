#Complete the function to return:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: You can resolve this exercise either importing the math module or without it 

import math

def apple_sharing(n,k):
  numero_manzanas = round(k / n)

  manzanas_restantes = k % n

  return numero_manzanas , manzanas_restantes
 

#Print the two answer per the example output.
print(apple_sharing(6,50))


# OTRA SOLUCION
# def apple_sharing(n,k):
#   numero_manzanas = math.trunc(k / n)

#   manzanas_restantes = k - (numero_manzanas * n)
  
#   return numero_manzanas , manzanas_restantes

# OTRA SOLUCION
# def apple_sharing(n,k):
#   numero_manzanas = math.floor(k / n)

#   manzanas_restantes = k - (numero_manzanas * n)
  
#   return numero_manzanas , manzanas_restantes