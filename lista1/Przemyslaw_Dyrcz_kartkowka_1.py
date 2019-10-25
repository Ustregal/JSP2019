#kartkowka 18.10.2019

#zad1
print("Zadanie 1")
print("")
print("podaj a")
a = input()
a = int(a)
print("podaj b")
b = input()
b = int(b)

if a < b:
    print("wartosc b musi byc mniejsza od a")
    print("podaj b")
    b = input()
    b = int(b)

Dzielenie = int(a/b)
reszta_z_dzielenia = a - b*Dzielenie
print("reszta z dzielenia =", int(reszta_z_dzielenia))


#zad2
print("")
print("zadanie 2")
print("")
print("podaj kat a")
a = input()
a = float(a)

print("podaj kat b")
b = input()
b = float(b)

print("podaj kat c")
c = input()
c = float(c)

#c^2 = a^2 + b^2 - 2ab cos(kat(a,b))
import numpy as np

cosinusab = (a**2. + b**2. - c**2.)/(2.*a*b)
kat = np.arccos(cosinusab)
kat = (kat*180/np.pi)
print("kat miedzy a i b =",kat)