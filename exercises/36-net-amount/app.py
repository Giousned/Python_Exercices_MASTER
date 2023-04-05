
def net_amount(transaction):

    deposito = 0
    retirada = 0
    array = transaction.split(" ")
    amount = 0

    for i in range(len(array)):
        if array[i] == "D":
            deposito += int(array[i+1])
        elif array[i] == "W":
            retirada += int(array[i+1])

    amount = deposito - retirada

    return amount


print(net_amount("D 300 D 300 W 200 D 100"))



# SOLUCION DADA
# def net_amount(param):
#     netAmount = 0
#     values = param.split()
#     for x in range(len(values)):
#         if values[x] == 'D':
#             netAmount+=int(values[x+1])
#         elif values[x] == 'W':
#             netAmount-=int(values[x+1])
#     return netAmount