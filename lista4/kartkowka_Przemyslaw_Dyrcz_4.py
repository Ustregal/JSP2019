# kartkowka 4

lista = [20,11,[5,-8],[1,-20],5,[-19,-8],-10,[7,-19],-15,[6,-12],[-17,9],2]

lista_int = [item for item in lista if isinstance(item, int)]
lista_list = [item for item in lista if isinstance(item, list)]

#print(lista_int)
#print(lista_list)

def sortowanie(jakaslista):
    return sorted(jakaslista, key=abs)

def sortowanie_list(jakaslista):
    return sorted(jakaslista, key=lambda x: abs(x[0]))

#print(sortowanie(lista_int))
lista_int_sort = sortowanie(lista_int)

#print(sortowanie_list(lista_list))
lista_list_sort = sortowanie_list(lista_list)

lista_ostateczna = lista_int_sort + lista_list_sort
print(lista_ostateczna)