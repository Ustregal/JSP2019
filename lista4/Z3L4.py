# zad 3 lista 4

import numpy as np

print("podaj kat")
kat = float(input())

def przelicznik_na_rad(a):
    return a*np.pi/180.

def przelicznik_na_deg(b):
    return b*180./np.pi

print("czy chcesz przeliczyc kat na radiany czy stopnie? (rad/deg)")
tak = input()
tak = str(tak)

if tak=="rad" or tak=="radian" or tak=="radiany":
    print("podany kat w radianach =", przelicznik_na_rad(kat))
elif tak=="deg" or tak=="degrees" or tak=="stopnie":
    print("podany kat w stopniach =", przelicznik_na_deg(kat))
else:
    print("wtf?")