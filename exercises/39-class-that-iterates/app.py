
# SOLUCION DADA

str_final = ""

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield(j)

for i in putNumbers(300):
    print(i)
    str_final += str(f'''{i} ''')

