# zad 1 lista 4

import numpy as np

lista = [1,2,3,4,5,6,7,8,9]

print("czy chcesz policzyc sume elementow listy? (y/n)")
tak = input()
tak = str(tak)

if tak=="y" or tak=="yes":
    print("suma elementow z listy =", sum(lista))
elif tak=="n" or tak=="no":
    print()
else:
    print("wtf?")

print("czy chcesz policzyc iloczyn elementow listy? (y/n)")
tak = input()
tak = str(tak)

def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  

if tak=="y" or tak=="yes":
    print("iloczyn elementow z listy =", multiply(lista))
elif tak=="n" or tak=="no":
    print()
else:
    print("wtf?")