# -*- coding: utf-8 -*-

# zad 2 lista 8

import datetime
import sys
import os
import SzyfrCezara as sc

n = input("jakiego kodowania szukasz (1-10)? ")
Y = input("ktory rok? ")
m = input("ktory miesiac? ")
d = input("ktory dzien? ")

name = str(n)+str(Y)+str(m)+str(d)

plik2 = 'plik_zaszyfrowany%s.txt' % name

odp = input("chcesz szukac katalogu z szyframi? (T/N): ")

if odp == "T":
    sciezka = input("Podaj pelna sciezke: ")
elif odp == "N" or "n":
    sciezka= "P:\Materiały naukowe\dziewiąty semestr - materiały\Python\Ćwiczenia\Lista 8"


plik = plik2
try:
    f = open(plik, 'rb')
except OSError:
    print("nie mozna odtworzyc pliku:", plik)
    sys.exit()

with open(os.path.join(sciezka, plik2), "r") as file2:
    szyfr = file2.read()

#print(szyfr)

tekst_rozsz = sc.rozszyfruj(int(n), szyfr)
print(tekst_rozsz)

plik3 = 'plik_rozszyfrowany%s.txt' % name
with open(os.path.join(sciezka, plik3), "w") as file3:
    file3.write(tekst_rozsz)

file2.close()
file3.close()