# zad 2 lista 5

liczba1 = list(input())
liczba1.reverse ()
tysiace = ('tysiac','tysiace','tysiecy')
setki = ('sto','dwiescie','trzysta','czterysta','piecset','szeset','siedemset','osiemset','dziewiecset')
cyfry = ('zero','jeden','dwa','trzy','cztery','piec','szesc','siedem','osiem','dziewiec','dziesiec','jedenascie','dwanascie','trzynascie','czternascie','pietnascie','szesnascie','siedemnascie','osiemnascie','dziewietnascie')
dziesiatki = ('dwadziescia','trzydziesci','czterdziesci','piecdziesiat','szescdziesiat','siedemdziesiat','osiemdziesiat','dziewiecdziesiat')
slownie = []
for nr, cyfra in enumerate (liczba1):
    if nr in {0,3,6,9}:
        if nr == 3:
            if len (liczba1) > 4 and int (liczba1[nr+1]) == 1:
                slownie.insert (0, tysiace[2])                
            elif 1 < int (cyfra) < 5:
                slownie.insert (0, tysiace[1])
            else:
                slownie.insert (0, tysiace[2])
        if nr+1 < len (liczba1):
            if int (liczba1[nr+1]) > 1:               
                if int (cyfra) == 0:
                    continue
                else:
                    slownie.insert (0, cyfry[int (cyfra)])
            else:
                if int (cyfra) == 0:
                    continue
                else:
                    slownie.insert (0, cyfry[ int(liczba1 [nr+1]+ liczba1 [nr])])
        else:
            if nr > 0 and int (cyfra) == 1:
                if nr == 3:
                    slownie.insert (0, tysiace[0])
            else:
                slownie.insert (0, cyfry [int (cyfra)])
    elif nr in {1,4,7,10}:
        if int(cyfra) == 1 or int (cyfra) == 0:
            continue
        else:
            slownie.insert (0, dziesiatki[ int (cyfra)-2])
    elif nr in {2,5,8,11}:
        if int (cyfra) == 0:
            continue
        else:
            slownie.insert (0, setki[ int (cyfra)-1])
print ("Slownie:"," ".join(slownie))