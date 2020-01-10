# zad 1 lista 10

import numpy as np

r = float(input("podaj promien: "))

class Kolo:
  def __init__(nazwa, obwod, pole):
    nazwa.obwod = 2.*np.pi*r
    nazwa.pole = np.pi*(r)**2.

p = Kolo("nazwa", r)

print("obwod kola o promieniu r =", r, "wynosi:", p.obwod)
print("pole kola o promieniu r =", r, "wynosi:", p.pole)
