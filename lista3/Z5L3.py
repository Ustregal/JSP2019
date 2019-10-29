# zad 5 lista 3

import re

print("wprowadz nowe haslo")
haslo = input()
haslo = str(haslo)
#print(haslo)
#print(type(haslo[0]))

#malelitery = ["a","e","i","o","u","y","b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","w","v","x","z"]
#duzelitery = ["A","E","I","O","U","Y","B","C","D","F","G","H","J","K","L","M","N","P","R","S","T","W","V","X","Z"]

def main(): 
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,16}$"
    pat = re.compile(reg)                  
    mat = re.search(pat, haslo) 
    if mat: 
        print("Prawidlowe haslo")
    else: 
        print("Nieprawidlowe haslo.")
        print("haslo mus zawierac 6-16 znakow, przynajmniej jedna mala i duza litere alfabetu, cyfre, znak specjalny znak z Japonskiego alfabetu Kanji, obrazek clipart, podanie o przedluzenie sesji i krew dziewicy")
        print("zrestartuj program")     

if __name__ == '__main__': 
    main() 