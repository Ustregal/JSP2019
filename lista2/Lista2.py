print("Zad 1")

#w kolumnie:
#for i in range(20):
#    print(1.2e+3+34.5,";")

print("")
#w jednej linii
print(str(1.2e+3+34.5)*20, ";")

print("[ wcisnij enter ]")
input()

print("Zad 2")
print("")

print("podaj wyraz")
napis = input()
for i in range(30):
    print(napis)

print("[ wcisnij enter ]")
input()
print("Zad 3")
print("")

print("podaj napis")
napis = input()
napis = list(napis)
n = len(napis)
print(napis[0]+napis[1]+napis[n-2]+napis[n-1])

print("[ wcisnij enter ]")
input()

#zad 4, 5, 6 w osobnych programach

print("Zad 7")
print("")

lista = [(2,8),(5,5),(9,3),(1,0),(3,2),(6,4),(1,9),(10,3),(2,3),(1,7)]

lista = sorted(lista, key=lambda x: x[1])
print(lista)

print("[ wcisnij enter ]")
input()
print("Zad 8")
print("")

znaki = ("B", "A", "J", "D", "O", "N")
x = "".join(znaki)
print(x)

print("[ wcisnij enter ]")
input()
print("Zad 9")
print("")

import itertools as it

lista = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
listapodzielona = list(it.chain(*lista))
print("podzielona lista:")
print(listapodzielona)

#zad 10 w osobnym programie

print("")
print("koniec")