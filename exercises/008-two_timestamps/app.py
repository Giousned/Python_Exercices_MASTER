#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):

    diff_horas = hr2 - hr1

    diff_min = min2 - min1

    diff_sec = sec2 - sec1

    segundos_totales = diff_horas * 3600 + diff_min * 60 + diff_sec * 1

    return segundos_totales


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))