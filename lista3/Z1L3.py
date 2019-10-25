#zad 1 lista 3

samogloski = ["a","e","i","o","u","y"]
spolgloski = ["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","w","v","x","z"]
znaki = samogloski + spolgloski
#print(znaki)

print("podaj litere")
litera = input()
litera = str(litera)

if litera not in znaki:
    print("podany znak nie jest litera alfabetu lacinskiego")
elif litera in samogloski:
    print("podana litera jest samogloska")
else:
    print("podana litera jest spolgloska")