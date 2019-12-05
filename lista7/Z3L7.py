# zad 3 lista 7

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

for i in range(len(n)-1, 0, -1):
    for j in range(i):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
print(n)

end = time.time()
total = end - start

print("Czas wykonywania:","{0:02f}s".format(total))