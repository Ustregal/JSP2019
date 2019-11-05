# zad 9 lista 4

print("podaj n")
n = int(input())

fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 

if n>0 or n==0:
    print ("silnia z", n, "=",end="") 
    print (fact)
else:
    print("niewlasciwa wartosc n")