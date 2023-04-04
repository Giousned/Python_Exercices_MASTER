
def each_digit_even(num1, num2):

    digit1 = 0
    digit2 = 0
    digit3 = 0
    digit4 = 0

    array = []

    for i in range(num1, num2+1, 1):

        digit1 = int(i / 1000) % 10
        digit2 = int(i / 100) % 10
        digit3 = int(i / 10) % 10
        digit4 = i % 10

        # print(digit1)
        # print(digit2)
        # print(digit3)
        # print(digit4)

        if digit1 % 2 == 0 and digit2 % 2 == 0 and digit3 % 2 == 0 and digit4 % 2 == 0:
            array.append(str(i))

    return (",".join(array))


print(each_digit_even(1000, 3000))



# SOLUCION DADA

# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print ",".join(values)