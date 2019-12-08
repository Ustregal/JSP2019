# zad 3 lista 8

import random

rok = int(input("podaj cyframi rok urodzenia: "))
miesiac = input("podaj cyframi miesiac urodzenia: ")
dzien = input("podaj cyframi dzien urodzenia: ")
plec = input("podaj swoja plec (M/K): ")

plik = open('numer_pesel.txt', mode='w')
print("twoje wygenerowane numery pesel: ")

for i in range(10):
    rokstr = str(rok)
    rokstr = rokstr[2] + rokstr[3]
    #print(rokstr)

    dzienint = int(dzien)
    miesiacint = int(miesiac)

    if dzienint<10:
        dzien = "0"+str(dzienint)

    if miesiacint<10:
        miesiac = "0"+str(miesiacint)

    if rok>=2000:
        miesiac = str(int(miesiac)+20)
    else:
        miesiac = str(miesiac)

    if plec == "K":
        plec = [0,2,4,6,8]
    elif plec == "M":
        plec = [1,3,5,7,9]

    pesel1 = rokstr + miesiac + dzien
    #print(pesel1)

    lista = [0,1,2,3,4,5,6,7,8,9]
    a = random.choice(lista)
    b = random.choice(lista)
    c = random.choice(lista)
    d = random.choice(plec)

    wyrazenie = 9*int(pesel1[0]) + 7*int(pesel1[1]) + 3*int(pesel1[2]) + 1*int(pesel1[3]) + 9*int(pesel1[4]) + 7*int(pesel1[5]) + 3*a + 1*b + 9*c + 7*d
    kontrolna = wyrazenie % 10
    #print(kontrolna)
    pesel2 = pesel1 + str(a) + str(b) + str(c) + str(d) + str(kontrolna)
    
    print(pesel2)
    plik.write(pesel2 + '\n')

plik.close() 