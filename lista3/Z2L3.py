#zad 2 lista 3

print("podaj liczbe")
liczba = input()

liczba = float(liczba)

r = int(liczba%2)

lista_odpowiedzi = ["parzysta","nieparzysta"]
print("podana liczba jest", lista_odpowiedzi[r])