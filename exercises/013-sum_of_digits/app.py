#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  
  centenas = (num)//100 % 10
  decenas = (num)//10 % 10
  unidades = num % 10

  suma_total = centenas + decenas + unidades

  return suma_total


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))


# OTRA SOLUCION
# def digits_sum(num):
  
#   centenas = str(num)[-3] 
#   decenas = str(num)[-2]
#   unidades = str(num)[-1]

#   suma_total = int(centenas) + int(decenas) + int(unidades)

#   return suma_total


# SOLUCION DADA
# def digits_sum(num):
#   aux = 0
#   for x in str(num):
#     aux= aux+int(x)
#   return aux