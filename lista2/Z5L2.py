print("podaj wyraz")
napis = input()

n = len(napis)
srodek = round(n/2)
#print(srodek)
napis2 = "[WALL]"
print(napis[0:srodek] + napis2 + napis[srodek:n])