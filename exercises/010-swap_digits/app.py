#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  string = str(num)

  entero_final = int(string[1]+string[0])
  
  return entero_final
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))


# OTRA SOLUCION
# def swap_digits(num):
#   # Your code here
#   digito1 = int(num / 10)

#   digito2 = num % 10

#   string = f"{digito2}{digito1}"

#   entero_final = int(string)
  
#   return entero_final


# SOLUCION DADA
# def swap_digits(num):
#   # Your code here
#   aux = str(num)[1] +str(num)[0]
  
#   return int(aux)
