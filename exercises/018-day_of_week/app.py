#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):

  dia_semana = k % 7

  print((3+k)%7)

  if dia_semana == 1:
    return 4
  elif dia_semana == 2:
    return 5
  elif dia_semana == 3:
    return 6
  elif dia_semana == 4:
    return 0
  elif dia_semana == 5:
    return 1
  elif dia_semana == 6:
    return 2
  elif dia_semana == 0:
    return 3




#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(1))


# SOLUCION DADA
# def day_of_week(k):
  
#   return (3+k)%7