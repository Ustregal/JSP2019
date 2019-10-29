# zad 7 lista 3

print("podaj numer do ktorego maja byc wymienione wyrazy szeregu Fibonacciego")
N = int(input())
print()

def Fibonacci(n): 
    if n<0: 
        print("nie wlasciwa wartosc, musi byc wieksza od 0") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

for i in range(1,N+1):
    print(Fibonacci(i)) 