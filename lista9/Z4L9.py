# -*- coding: utf-8 -*-

# zad 4 lista 9

import matplotlib.pyplot as plt

def read_col(fname, col, convert, sep):
    with open(fname) as fobj:
        return [convert(line.split(sep=sep)[col]) for line in fobj]

nazwa = read_col('jezyki.txt', 1, str, None)
print(nazwa)

popularnosc = read_col('jezyki.txt', 2, float, None)
print(popularnosc)

pozostale = 100. - sum(popularnosc)
nazwa.append("pozostałe")
popularnosc.append(pozostale)

plt.title("Najpopularniejsze języki programowania")
plt.ylabel("użytkowanie [%]")
plt.bar(nazwa,popularnosc, color="green") #x - nazwy, y - wartosci
plt.show()