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
    print("wyraz nr", n, "ciagu geometrycznego o q =", q, "i a1 =", a1, "jest rowny:")
    print(ciag_geometryczny(int(a1),int(q),n))
elif q == "":
    q = 2
    print("wyraz nr", n, "ciagu geometrycznego o q =", q, "i a1 =", a1, "jest rowny:")
    print(ciag_geometryczny(int(a1),int(q),n))
elif (q == "" and a1 == ""):#problem z tym elif
    q = 2
    a1 = 1
    print("wyraz nr", n, "ciagu geometrycznego o q =", q, "i a1 =", a1, "jest rowny:")
    print(ciag_geometryczny(int(a1),int(q),n))    
else:
    print("wyraz nr", n, "ciagu geometrycznego o q =", q, "i a1 =", a1, "jest rowny:")
    print(ciag_geometryczny(int(a1),int(q),n))
