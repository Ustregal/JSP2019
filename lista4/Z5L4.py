# zad 5 lista 4

lista = [2,5,7,9]


def permutation(lst): 
    if len(lst) == 0: 
        return [] 
    if len(lst) == 1: 
        return [lst] 
    l = []
    for i in range(len(lst)): 
        m = lst[i] 
        remLst = lst[:i] + lst[i+1:] 
        for p in permutation(remLst): 
            l.append([m] + p) 
    return l 

 
for p in permutation(lista): 
    print(p)