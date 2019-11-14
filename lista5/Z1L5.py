# zad 1 lista 5

def text2int(textnum, numwords={}):
    if not numwords:
        units = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem",
        "dziewiec", "dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie",
        "szesnascie", "siedemnascie", "osiemanscie", "dziewietnascie",]

        tens = ["", "", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]

        scales = ["sto", "tysiac", "milion", "miliard", "bilion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("nie poprawna nazwa: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

#print(text2int("seven billion one hundred million thirty one thousand three hundred thirty seven"))
#7100031337

#print(text2int("piec"))

print("podaj liczbe slownie bez znakow polskich")
tekst = str(input())
print(text2int(tekst))