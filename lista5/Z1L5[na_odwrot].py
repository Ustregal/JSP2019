# zad 1 lista 5

print("podaj liczbe naturalna (0 - 59)")
numer = int(input())

def int_to_en(num):
    d = { 0 : 'zero', 1 : 'jeden', 2 : 'dwa', 3 : 'trzy', 4 : 'cztery', 5 : 'piec', 6 : 'szesc', 7 : 'siedem', 8 : 'osiem', 9 : 'dziewiec', 10 : 'dziesiec',
          11 : 'jedenascie', 12 : 'dwanascie', 13 : 'trzynascie', 14 : 'czternascie', 15 : 'pietnascie', 16 : 'szesnascie', 17 : 'siedemnascie', 18 : 'osiemnascie',
          19 : 'dziewietnascie', 20 : 'dwadziecia', 30 : 'trzydziesci', 40 : 'czterdziesci', 50 : 'piecdziesiat', 60 : 'szescdziesiat'}
    k = 1000
    assert(0 <= num)
    if (num < 20):
        return d[num]
    if (num > 20):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + ' ' + d[num % 10]
    raise AssertionError('num is too large:', str(num))

print(int_to_en(numer))