print("podaj wyraz z malej litery")
wyraz = input()

znak = wyraz[0]
print("pierwszy znak:", znak)

x = wyraz.replace(znak, "$")
#print(x)

print(znak + x[1:])
