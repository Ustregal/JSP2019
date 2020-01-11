# zad 3 lista 10

class wszystkie0():
    def __init__(self,lista):
        self.lista = lista
    def znajdz0(self):
        hashmap = {}
        out = []
        subarrays = []
        sum1 = 0
        for i in range(len(self.lista)):
            sum1 += self.lista[i]
            if sum1 == 0:
                out.append((0,i))
            al = []
            if sum1 in hashmap:
                al = hashmap.get(sum1)
                for it in range(len(al)):
                    out.append((al[it]+1,i))
            al.append(i)
            hashmap[sum1]=al
        for i in out:
            subarrays.append(self.lista[i[0]:i[1]+1])
        return subarrays

lista = [6,3,-1,-3,4,-2,2,4,6,-12,-7]
zera = wszystkie0(lista)
print("Wszystkie podlisty, ktorych suma wynosi 0 to:")
print(zera.znajdz0())