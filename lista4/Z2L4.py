# zad 2 lista 4

lista = [] 

n = int(input("Podaj ilosc elementow ")) 

for i in range(0, n): 
    ele = int(input()) 
    lista.append(ele)

#print(lista)
print()

lista = list(dict.fromkeys(lista))
print("lista bez powtorek:")
print(lista)