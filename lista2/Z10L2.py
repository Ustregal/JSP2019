print("a)")

x = range(0, 100, 3)
lista = []

for i in x:
    lista.append(i)

print(lista)

print("")
#===========
print("b)")

lista2 = lista
#print(lista2)
n = len(lista2)

b = int(n - (n-4)/3) #dlugosc koncowej listy

for i in range(4,b,2):
    del lista2[i]
    
print(lista2)
#print(len(lista2))

print("")
#===========
print("c)")

suma = sum(lista2)
srednia = suma/len(lista2)
print(srednia)
