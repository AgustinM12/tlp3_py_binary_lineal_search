from create_list import create_random_list as crl

# * DEFINICION DE LA FUNCION PARA LA BUSQUEDA LINEAL
def lineal_search(list,n, x):
# * SE RECORRE LA LISTA HASTA ENCONTRAR EL ELEMENTO X
    for i in range(0, n):
        if list[i] == x:
            return i
    return -1


# * PRUEBA INDIVIDUAL
# list=crl(10, 0, 10)

# x = 5

# result = lineal_search(list, len(list), x)

# if result == -1:    
#     print("Element: ", x, " not found in list: ", list)
# else:
#     print("Element: ", x, " is at index: ", result, " in list: ", list)