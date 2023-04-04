
def remove_duplicate_words(input_words):

    set_words = {}
    
    words = [word for word in input_words.split(" ")]

    set_words = set(words)

    array_ordered = sorted(list(set_words))

    return (" ".join(array_ordered))

print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))



# SOLUCION DADA, NO CREO QUE PASE EL TEST PORQUE NI LLAMA A LA FUNCION CREADA
# def remove_duplicate_words(text):
#     words = text.split()
#     return (" ".join(sorted(list(set(words)))))