print("zad 1")

krotka = (1,"a",2,"b")

print(krotka)
print(str(krotka[0])+str(krotka[1])+str(krotka[2])+str(krotka[3]))

#x = "".join(krotka)
#print(x)

print("")
print("zad 2")
lista = [1,1,2,4,6,5,3,1]
a = min(lista)
b = max(lista)
#print(a, b)

print("pierwsza minimalna wartosc w liscie:", lista.index(a))
print("pierwsza maksymalna wartosc w liscie:", lista.index(b))