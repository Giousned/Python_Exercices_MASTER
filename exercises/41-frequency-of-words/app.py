
# SOLUCION DADA

def words_output(string):

    freq = {}   # frequency of words in text
    str_final = ""
    # line = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

    for word in string.split():
        freq[word] = freq.get(word,0)+1

    words = list(freq.keys())
    # sorted(words)
    words.sort()

    for w in words:
        str_final += ("%s:%d " % (w, freq[w]))

    return str_final.rstrip()

words_output("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")