
def square_odd_numbers(string):

    array_final = []

    lista = string.split(",")

    for i in lista:
        if int(i) % 2 != 0:
            array_final.append(str(i))
    
    return (",".join(array_final))


print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))
print(square_odd_numbers("10,21,32,43,54,65,76,87,98"))




# SOLUCION DADA
# values = raw_input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print ",".join(numbers)
