# zad 1 lista 11

import urllib.request

strona = input("podaj adres strony: ")
#strona = "http://www.stackoverflow.com"

odp = str(urllib.request.urlopen(strona).getcode())

if odp == "200":
    print("tak, jest")
else:
    print("nie, nie ma")