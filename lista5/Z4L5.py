# zad 4 lista 5

print("napisz cos")
t1 = str(input())
print("chcesz zaszyfrowac (za) czy odszyfrowac (od) ?")
odp = str(input())

def zaszyfrowane(tekst):
    if odp =="za":
        return tekst.translate(str.maketrans({"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e"}))
    elif odp =="od":
        return tekst.translate(str.maketrans({"y" : "a", "i" : "e", "o" : "i", "a" : "o", "e" : "y"}))
    else:
        return print("wtf?") 

print("zaszyfrowane:",zaszyfrowane(t1))