
# SOLUCION DADA
values_string=input().strip()
l=values_string.split(",")
t=tuple(l)
print(l)
print(t)


values = input("")
valores = values.strip()
t=tuple(valores.split(','))
l=list(t)
print(l)
print(t)


# PROBAR CON ESTAS IDEAS
# def sequence_of_words(words):
#     items=[x for x in "{}".format(words).split(',')]
#     items.sort()
#     return (','.join(items))



# MI SOLUCION, SIN INPUT Y CON FUNCION
# def lista_tupla(string):

#     lista = []

#     lista = string.split(",")
    
#     tupla = ()

#     tupla = tuple(lista)

#     return f"{lista}\n{tupla}\n"

# print(lista_tupla("34,67,55,33,12,98"))