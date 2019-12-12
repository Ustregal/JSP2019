# -*- coding: utf-8 -*-

# zad 1 lista 8

import datetime
import sys
import os
import SzyfrCezara as sc

plik = 'plik_do_szyfrowania.txt'

try:
    f = open(plik, 'rb')
except OSError:
    print("nie mozna odtworzyc pliku:", plik)
    sys.exit()


with open('plik_do_szyfrowania.txt', 'r') as plik:
    #czepia się o "ł" i " - "
    tekst = plik.read()

#print(tekst)

przesun = int(input("Wprowadz klucz: "))
print(sc.wszystko(tekst, przesun))

#=====================================================
tekst_zasz = sc.zaszyfruj(przesun, tekst)

n = przesun
x = datetime.datetime.now()
Y = x.year
m = x.month
d = x.day

name = str(n)+str(Y)+str(m)+str(d)

plik2 = 'plik_zaszyfrowany%s.txt' % name
#plik2.write(tekst_zasz)
print(plik2)

odp = input("chcesz wybrac katalog do zapisania szyfru? (T/N): ")

if odp == "T":
    sciezka = input("Podaj pelna sciezke: ")
elif odp == "N" or "n":
    sciezka= "P:\Materiały naukowe\dziewiąty semestr - materiały\Python\Ćwiczenia\Lista 8"

with open(os.path.join(sciezka, plik2), "w") as file2:
    file2.write(tekst_zasz)

plik.close()
file2.close()