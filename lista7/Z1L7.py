# zad 1 lista 7

N = int(input("podaj ilosc elementow N: "))

# z petla for

def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("nie wlasciwa wartosc") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else:
        for i in range(1,n+1):
            c = a + b
            a = b
            b = c
            print(a)

print("petla: ", fibonacci(N)) 

#======================================================
# rekurencyjnie

def Fibonacci(n): 
    if n<0: 
        print("nie wlasciwa wartosc") 
    elif n==1: 
        return 0 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

if N>0:
    for i in range(1,N+1):
        print(Fibonacci(i))
elif N==0: 
    print(a)

print("rekurencja: ",Fibonacci(N))