#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  string = str(num)

  entero_final = int(string[1]+string[0])
  
  return entero_final
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))
