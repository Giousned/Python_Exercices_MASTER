
#SOLUCION DADA
from operator import itemgetter, attrgetter
def sort_tuples_ascending(tuples):
    l = []
    l.append(tuple(tuples.split(" ")))
    return (sorted(l))

print(sort_tuples_ascending("Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85"))
print(sort_tuples_ascending("Martin,23,30 Tomas,25,27"))



# MI SOLUCION QUE NO FUNCIONA
# def sort_tuples_ascending(lista):

#     lista.sort()

#     # for i in lista

#     return lista

# print(sort_tuples_ascending([('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Jason', '21', '85'), ('Tom', '19', '80')]))