
# SOLUCION DADA
def sequence_of_words(words):
    items=[x for x in "{}".format(words).split(',')]
    items.sort()
    return (','.join(items))


# MI SOLUCION, QUE NO SE PORQUE NO VA
# def sorted_names(sequence_of_words):

#     array = []

#     array = sequence_of_words.split(",")

#     array.sort()

#     string = ','.join(str(x) for x in array)

#     return string

# print(sorted_names("without,hello,bag,world"))