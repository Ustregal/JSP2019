import cmath 
import numpy as np

print("podaj oba argumenty liczby zespolonej")
x = input()
y = input()

x = int(x)
y = int(y)
  
z = complex(x,y)

sinz = np.sin(z)
cosz = np.cos(z)

print("Czesc rzeczywista sin(z): ",end="") 
print(sinz.real) 
  
print("Czesc urojona sin(z): ",end="") 
print(sinz.imag) 

print("Czesc rzeczywista cos(z): ",end="") 
print(cosz.real) 
  
print("Czesc urojona cos(z): ",end="") 
print(cosz.imag) 

print("sin^2(z) + cos^2(z) =",(sinz)**2+(cosz)**2)
