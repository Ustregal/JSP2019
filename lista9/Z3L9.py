# zad 3 lista 9

import numpy as np
import matplotlib.pyplot as plt

v0=float(input("podaj predkosc poczatkowa: "))
deg=float(input("podaj kat rzutu: "))
rad=deg*np.pi/180
g=10

h=v0**2*np.sin(rad)**2/(2*g)
z=v0**2*np.sin(2*rad)/g
t=2*v0*np.sin(rad)/g

print()
print("maksymalna wysokosc: ",round(h,3),"m")
print("zasieg rzutu: ",round(z,3),"m")
print("Czas trwania lotu:",round(t,3),"s")

def polozenie(x,alpha,g,v0):
    return x*np.tan(alpha) - x**2*g/(2*v0**2*(np.cos(alpha))**2)

x = np.linspace(-50,50,100)

plt.plot(x, polozenie(x,rad,g,v0))
#plt.subplot(3,1)
plt.show()