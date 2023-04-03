#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):

    dolares = int(d * n)

    centavos = int(c * n)

    if centavos > 100:
        centimos = centavos % 100
        dolares_añadidos = round(centavos / 100)
        dolares += dolares_añadidos
    else:
        centimos =  centavos

    return dolares, centimos
    


#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(10,55,2))


# SOLUCION DADA
# def total_cost(d,c,n):
#     return ((((d*100)+c)*n)//100, (((d*100)+c)*n)%100)
