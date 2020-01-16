# zad 4 lista 11

import re 

text = 'Gothic 3 - fabularna gra akcji, bezposrednia kontynuacja pierwszej i drugiej czesci serii Gothic, stworzona przez Piranha Bytes i wydana przez JoWooD Entertainment w 2006 roku. Marketing serii na anglojezycznych rynkach, a przede wszystkim w Stanach Zjednoczonych, byl niewielki.'
lista = re.findall(r'\b[ae]\w+\b',text)
print(lista)