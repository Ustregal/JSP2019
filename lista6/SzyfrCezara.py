# program szyfrujacy i deszyfrujacy 

alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ0123456789"
 
def zaszyfruj(przesuniecie, zdanie):
    wynik = ''
    for litera in zdanie:
        try:
            i = (alfabet.index(litera) + przesuniecie) % 77
            wynik += alfabet[i]
        except ValueError:
            wynik += litera
    return wynik
 
def rozszyfruj(przesuniecie, szyfr):
    wynik = ''
    for litera in szyfr:
        try:
            i = (alfabet.index(litera) - przesuniecie) % 77
            wynik += alfabet[i]
        except ValueError:
            wynik += litera
    return wynik
 
def wszystko(zdanie, przesuniecie):
    zaszyfrowany = zaszyfruj(przesuniecie, zdanie)
    rozszyfrowany = rozszyfruj(przesuniecie, zaszyfrowany)
 
    print ('Przesuniecie: %s' % przesuniecie)
    print ('Zdanie: %s' % zdanie)
    print ('Zaszyfrowany: %s' % zaszyfrowany)
    print ('Rozszyfrowany: %s' % rozszyfrowany)