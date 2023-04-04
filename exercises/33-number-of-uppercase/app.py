
def uppers_and_lowers(text):

    contar_lowers = 0
    contar_uppers = 0

    for i in text:
        if i.islower():
            contar_lowers += 1
        elif i.isupper():
            contar_uppers += 1

    return f"UPPER CASE {contar_uppers} LOWER CASE {contar_lowers}"

print(uppers_and_lowers("MY Name Is PepE and I LIVE iN thE NexT apartMent"))


# SOLUCION DADA
# s = raw_input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print "UPPER CASE", d["UPPER CASE"]
# print "LOWER CASE", d["LOWER CASE"]