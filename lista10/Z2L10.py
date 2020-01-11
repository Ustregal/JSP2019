# zad 2 lista 10

from itertools import combinations

l1 = [1, 2, 3]

class podlisty: 
    def sub_lists(my_list):
        subs = []
        for i in range(0, len(my_list)+1):
            temp = [list(x) for x in combinations(my_list, i)]
            if len(temp)>0:
                subs.extend(temp)
        return subs

print(podlisty.sub_lists(l1))