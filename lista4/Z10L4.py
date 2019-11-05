# zad 10 lista 4

print("podaj a")
a = int(input())

print("podaj b")
b = int(input())

def dzielnik(a,b): 
    if(b==0): 
        return a 
    else: 
        return dzielnik(b,a%b) 
 
print(dzielnik(a,b)) 