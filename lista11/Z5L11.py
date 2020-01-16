# zad 5 lista 11

import re 

text = 'Gothic 3 - fabularna gra akcji, bezposrednia kontynuacja pierwszej i drugiej czesci seriiGothic, stworzona przezPiranhaBytes i wydana przezJoWooD Entertainment w 2006 roku.Marketing serii na anglojezycznych rynkach, a przede wszystkim wStanachZjednoczonych, byl niewielki.'

poprawiony = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
print(poprawiony)