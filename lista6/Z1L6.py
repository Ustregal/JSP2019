# zad 1 lista 6

import trojkat as tr

#print(tr.obwod(1,2,2))

print("podaj boki trojkata: a, b, c")
A = float(input())
B = float(input())
C = float(input())

print("obwod trojkata abc:", tr.obwod(A,B,C))
print("pole trojkata abc:", tr.pole(A,B,C))
print("analiza bokow trojkata:")
print(tr.analiza_ramion(A,B,C))
print("analiza katow trojkata:")
print(tr.analiza_katow(A,B,C))