
print("podaj a")
a = input()
a = int(a)
print("podaj b")
b = input()
b = int(b)

while a < b:
	print("wartosc b musi byc mniejsza od a")
	print("podaj b")
	b = input()
	b = int(b)
	
Dzielenie = int(a/b)
print("a/b =", Dzielenie)
reszta_z_dzielenia = a - b*Dzielenie
print("reszta z dzielenia =", reszta_z_dzielenia)

Z = reszta_z_dzielenia
wynik = Z*(Z+3)
print("Z*(Z+3) =",wynik)
