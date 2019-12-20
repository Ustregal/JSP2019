# zad 2 lista 9

import numpy as np

print("podaj dane pomiarowe (nazwe pliku plik.txt albo recznie po spacji):")
dane1 = input()
print()

#dane2 = list(map(int,dane1.split()))
if ".txt" in dane1:
    print(dane1)
    
    with open(dane1, 'r') as plik:
        tekst = plik.readlines()
        tekst = [line.rstrip('\n') for line in open(dane1)]
        tekst = list(map(int, tekst))
        print(tekst)
else:
    tekst = list(map(int,dane1.split()))
    print(tekst)

print("srednia: ", np.mean(tekst))
print("wariancja: ", np.var(tekst))
print("odchylenie standardowe: ", np.std(tekst))
