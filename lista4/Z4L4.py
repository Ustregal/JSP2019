# zad 4 lista 4

def ciag_geometryczny(a1,q,n):
    return a1*q**(n-1)


print("podaj wartosc pierwszego elementu ciagu geometrycznego a1 (domyslne 1):")
a1 = input()

print("podaj wartosc iloczynu ciagu geometrycznego q (domyslne 2):")
q = input()

print("podaj nunmer interesujacego cie elementu ciagu geometrycznego n:")
n = int(input())

if a1 == "":
    a1 = 1

if q == "":
    q = 2

if (q == "" and a1 == ""):
    q = 2
    a1 = 1

print("wyraz nr", n, "ciagu geometrycznego o q =", q, "i a1 =", a1, "jest rowny:")
print(ciag_geometryczny(int(a1),int(q),n))