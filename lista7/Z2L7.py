# zad 2 lista 7

import random
import time

k = int(input("liczba elementow listy do posortowania: "))

start = time.time()
i = 0
n = []

while i<k:
    n.append(random.randint(0,20))
    i+=1
print(n)

for i in range(1,len(n)):
    klucz = n[i]
    j = i-1
    while j>=0 and n[j]>klucz:
        n[j+1] = n[j]
        j = j-1
    n[j+1] = klucz
print(n)

end = time.time()
total = end - start

print("Czas wykonywania:","{0:02f}s".format(total))