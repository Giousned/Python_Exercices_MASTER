import math

def print_formula(*num):

    string_final = ""
    array_final = []

    for i in num:
        array_final.append(round(math.sqrt(2*50*i/30)))

    string_final = ','.join(str(x) for x in array_final)

    return string_final


print(print_formula(100,150,180))





# MI SOLUCION, NO SE PORQUE DA ERROR

# def print_formula(values):

#     C = 50
#     H = 30

#     array_final = []

#     for i in values:
#         D = int(i)
#         result = math.sqrt((2 * C * D) / H)
#         array_final.append(int(result))

#     string_final = ','.join(str(x) for x in array_final)

#     return string_final



# print(print_formula(numeros_input))
