#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):

  numero_coma = (num * 10) % 10

  return round(numero_coma)


#Invoke the function with a positive real number. ex. 34.33
print(first_digit(34.33))


# SOLUCION DADA
# import math
# def first_digit(num):
#   return int(str(math.floor(num*10))[-1])