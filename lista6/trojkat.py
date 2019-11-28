# modul trojkat

#pole pow ze wzoru Herona
def pole(a,b,c):
    p = (float(a)+float(b)+float(c))/2.
    return (p*(p-a)*(p-b)*(p-c))**(0.5)

def obwod(a,b,c):
    return a+b+c

def analiza_ramion(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a==b and b==c:
        return print("oraz trojkat rownoboczny")
    elif a==b or a==c or b==c:
        return print("trojkat rownoramienny")    
    else:
        return print("trojakt nie jest rownoboczny ani rownoramienny")
        
def analiza_katow(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    lb = [a,b,c]
    lb.sort()
    p = ((lb[0])**2. + (lb[1])**2.)**(0.5)
    if lb[2]==p:
        return print("jest to trojkat prostokatny")
    elif lb[2] < p:
        return print("jest to trojkat ostrokatny")
    elif lb[2] > p:
        return print("jest to trojkat rozwartokatny")

#print(pole(1,2,2))
#print(obwod(1,2,2))
#print(analiza_ramion(1,2,2))
#print(analiza_katow(1,2,2))