
def generate_dict(num):

    diccionario = {}

    for i in range(1,num+1):
        diccionario[i] = i*i

    return diccionario


print(generate_dict(8))



# SOLUCION DADA
# def generate_dict(n):
#     d=dict()
#     for i in range(1,n+1):
#         d[i]=i*i
#     return d

# print(generate_dict(n))