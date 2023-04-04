
def lines(words):

    items = [x for x in "{}".format(words).upper().split(',')]

    return (' '.join(items))

print(lines("Hello world Practice makes perfect"))


# SOLUCION DADA
# def lines(text):
#     return text.upper()

# print(lines('Hello world'))