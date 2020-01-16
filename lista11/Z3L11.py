# zad 3 lista 11

import re 

text = 'Gothic 3 - fabularna gra akcji, bezposrednia kontynuacja pierwszej i drugiej czesci serii Gothic, stworzona przez Piranha Bytes i wydana przez https://www.youtube.com/channel/UCJfxNuV2bJTRzViK_kXn9pA/featured?view_as=subscriber w 2006 roku. Marketing serii na anglojezycznych rynkach, a przede wszystkim w Stanach Zjednoczonych, byl niewielki.'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

print("tekst: ",text)
print("adresy URL: ",urls)