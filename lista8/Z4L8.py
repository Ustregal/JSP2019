# zad 4 lista 8

parz = [0,2,4,6,8]
nparz = [1,3,5,7,9]

odp = input("chcesz sprawdzic nr. PESEL? T/N: ")

if odp == "T":
    numer = input("podaj numer: ")
    print("data urodzin:")
    datanr = int(numer[0:6])
    dziennr = str(datanr)[4:6]
    if int(str(datanr)[2:4])<20:
        miesiacnr = str(datanr)[2:4]
        roknr = "19" + str(datanr)[0:2]
    else:
        miesiacnr = str(int(str(datanr)[2:4]) - 20)
        roknr = "20" + str(datanr)[0:2]
    print(dziennr + "-" + miesiacnr + "-" + roknr)
    print("plec:")
    plec = int(numer[9])
    if plec in parz:
        print("Kobieta")
    elif plec in nparz:
        print("Mezczyzna")
    wyrazenie = 9*int(numer[0]) + 7*int(numer[1]) + 3*int(numer[2]) + 1*int(numer[3]) + 9*int(numer[4]) + 7*int(numer[5]) + 3*int(numer[6]) + 1*int(numer[7]) + 9*int(numer[8]) + 7*int(numer[9])
    kontrolna = wyrazenie % 10
    if int(numer[10]) != kontrolna:
        print("ten PESEL jest nie poprawny")
    else:
        print("NUMER POPRAWNY")

#===============================================
print("===============================================")

print("tworzymy liste korzystajac z programu do generowania nr PESEL")
import Z3L8

#===============================================
plik = open('numer_pesel.txt')
linie = [line.rstrip('\n') for line in plik]
print("Numery PESEL:")
print(linie)

#===============================================
for i in linie:
    #print(i[10])
    wyrazenie = 9*int(i[0]) + 7*int(i[1]) + 3*int(i[2]) + 1*int(i[3]) + 9*int(i[4]) + 7*int(i[5]) + 3*int(i[6]) + 1*int(i[7]) + 9*int(i[8]) + 7*int(i[9])
    kontrolna = wyrazenie % 10
    if int(i[10]) != kontrolna:
        print("ten PESEL jest nie poprawny", i)

#================================================
print("data urodzin:")
data = int(linie[0][0:6])
#print(data)

dzien = str(data)[4:6]
#print(dzien)

if int(str(data)[2:4])<20:
    miesiac = str(data)[2:4]
    rok = "19" + str(data)[0:2]
else:
    miesiac = str(int(str(data)[2:4]) - 20)
    rok = "20" + str(data)[0:2]

#print(miesiac)
#print(rok)

datapelna = dzien + "-" + miesiac + "-" + rok
print(datapelna)

#================================================
print("plec:")

plec = int(linie[0][9])
#print(plec)

if plec in parz:
    print("Kobieta")
    dopisek = datapelna + "    " + "Kobieta"
elif plec in nparz:
    print("Mezczyzna")
    dopisek = datapelna + "    " + "Mezczyzna"

#print(dopisek)
plik = open('numer_pesel.txt', "a")
plik.write(dopisek)

plik.close()