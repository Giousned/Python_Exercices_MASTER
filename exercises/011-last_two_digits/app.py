#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):

    ultimos_2_digitos = num % 100

    return ultimos_2_digitos

#Invoke the function with any interger greater than 9.
print(last_two_digits(1234))


# SOLUCION DADA
# : ES COMO EL SPREAD OPERATOR EN JS TE HACE UNA COPIA, Y PUEDES PONER 2 ARGUMENTOS, ANTES (INICIO DE LA COPIA), Y 
# DESPUES (FINAL DE LA COPIA SIN INCLUIR), O DEJARLO VACIO Y ES HASTA EL FINAL
# def last_two_digits(num):
#     if num > 9: return int(str(num)[-2:])
#     else: return num