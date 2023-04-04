
def letters_and_digits(text):

    contar_letras = 0
    contar_numero = 0

    for i in range(len(text)):
        if text[i].isalpha():
            contar_letras += 1
        if text[i].isdigit():
            contar_numero += 1

    return f"LETTERS {contar_letras} DIGITS {contar_numero}"

print(letters_and_digits("hello world! 123"))


# SOLUCION DADA
# def letters_and_digits(text):
#     d={"DIGITS":0, "LETTERS":0}
#     for c in text:
#         if c.isdigit():
#             d["DIGITS"]+=1
#         elif c.isalpha():
#             d["LETTERS"]+=1
#         else:
#             pass
    
#     return ("LETTERS {} DIGITS {}".format(d['LETTERS'], d['DIGITS']))