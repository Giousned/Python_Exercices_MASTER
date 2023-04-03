#Complete the function to return the tens digit of a given interger
def tens_digit(num):

  decenas = str(num)[-2]

  return int(decenas)


#Invoke the function with any interger.
print(tens_digit(1234))


# SOLUCION DADA
#  // TE DA EL RESULTADO DE LA DIVISION PERO REDONDEANDO EL RESULTADO HACIA ABAJO Y DANDO EL RESULTADO SIN DECIMALES
# def tens_digit(num):
#   return (num // 10) % 10
