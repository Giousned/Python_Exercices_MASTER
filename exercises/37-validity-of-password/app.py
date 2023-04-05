

def valid_password(passwords):

    array = passwords.split(",")
    valid_passwords = []

    for i in array:

        if len(i) >= 6 and len(i) <= 12:

            l, u, p, d = 0, 0, 0, 0

            for j in i:
                # counting lowercase alphabets
                if (j.islower()):
                    l += 1
        
                # counting uppercase alphabets
                if (j.isupper()):
                    u += 1
        
                # counting digits
                if (j.isdigit()):
                    d += 1
        
                # counting the mentioned special characters
                if(j=='$'or j=='#' or j=='@'):
                    p += 1

                if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l+p+u+d == len(i)):
                    valid_passwords.append(i)

    return (",".join(valid_passwords)) 


print(valid_password("R@m_f0rtu9e$,ABd1234@1,a F1#,2w3E*,2We3345"))


# SOLUCION DADA
# Module of regular expression is used with search()
# import re
# def valid_password(password):
#     value = []
#     items=[x for x in password.split(',')]
#     for p in items:
#         if len(p)<6 or len(p)>12:
#             continue
#         else:
#             pass
#         if not re.search("[a-z]",p):
#             continue
#         elif not re.search("[0-9]",p):
#             continue
#         elif not re.search("[A-Z]",p):
#             continue
#         elif not re.search("[$#@]",p):
#             continue
#         elif re.search("\s",p):           # \s encuentra espacios en blanco
#             continue
#         else:
#             pass
#         value.append(p)
#     return (",".join(value))


# SOLUCIONES DE INTERNET
# SOLUCION 1

# Module of regular expression is used with search()
# import re
# password = "R@m@_f0rtu9e$"
# flag = 0
# while True:
#     if (len(password)<=8):
#         flag = -1
#         break
#     elif not re.search("[a-z]", password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]" , password):
#         flag = -1
#         break
#     elif re.search("\s" , password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break
 
# if flag == -1:
#     print("Not a Valid Password ")



# SOLUCION 2

# l, u, p, d = 0, 0, 0, 0
# s = "R@m@_f0rtu9e$"
# capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# smallalphabets="abcdefghijklmnopqrstuvwxyz"
# specialchar="$@_"
# digits="0123456789"
# if (len(s) >= 8):
#     for i in s:
 
#         # counting lowercase alphabets
#         if (i in smallalphabets):
#             l+=1           
 
#         # counting uppercase alphabets
#         if (i in capitalalphabets):
#             u+=1           
 
#         # counting digits
#         if (i in digits):
#             d+=1           
 
#         # counting the mentioned special characters
#         if(i in specialchar):
#             p+=1       
# if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
#     print("Valid Password")
# else:
#     print("Invalid Password")
