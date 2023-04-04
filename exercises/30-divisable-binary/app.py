
# SOLUCION DADA
def divisable_binary(text):

    value=[]

    items = [x for x in text.split(',')]

    for p in items:
        intp = int(p, 2)
        
        if not intp%5:
            value.append(p)

    return (','.join(value))



# MI SOLUCION, QUE NO SE PORQUE NO PASA EL TEST
# def divisable_binary(text):

#     items = [x for x in text.split(',')]

#     lista = []

#     for i in items:
#         if int(i) % 5 == 0:
#             lista.append(str(i))

#     return (",".join(lista))

# print(divisable_binary("0100,0011,1010,1001"))