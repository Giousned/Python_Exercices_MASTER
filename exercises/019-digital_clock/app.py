#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):

  horas = round(n / 60)

  minutos = n % 60

  return horas, minutos

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))


# SOLUCION DADA
# def digital_clock(n):
#   return ((n // 60), (n % 60))
