lista = ["Kasia", "Basia", "Marek", "Darek"]


lista.append("Jozek")

Baby = ["Ania", "Basia"]
lista.extend(Baby)

#print(lista)
lista.sort()
print(lista)

print("czwarty student:", lista[3])
print("drugi i pierwszy student:", lista[0], ", ", lista[1])

n = len(lista)
print("przedostatni i ostatni student:", lista[n-2], ", ", lista[n-1])

basie = lista.count("Basia")
for i in range(basie):
    lista.remove("Basia")

print(lista)
m = len(lista)
print("ilosc studentow nie liczac Bas:", m)

lista = tuple(lista)
print(lista)