# zad 3 lista 3

print("Podaj wspolczynniki:")
print("podaj a")
a = input()
a = float(a)

print("podaj b")
b = input()
b = float(b)

print("podaj c")
c = input()
c = float(c)


if a==0 and b==0 and c==0:
    print("nieskonczenie miejsc zerowych")
elif a==0 and b==0 and c!=0:
    print("brak miejsc zerowych")
elif a==0 and b!=0:
    x=-b/c
    print("Miejsce zerowe =",x)
else:
    delta=b**2-4*a*c
    if delta > 0:
        x1=(-b-delta**(1/2))/(2*a)
        x2=(-b+delta**(1/2))/(2*a)
        print("Miejsca zerowe: x1 =",x1,"i x2 =",x2)
    elif delta == 0:
        x0=-b/(2*a)
        print("Miejsce zerowe:",x0)
    elif delta < 0:
        print("Brak rzeczywistych miejsc zerowych")
