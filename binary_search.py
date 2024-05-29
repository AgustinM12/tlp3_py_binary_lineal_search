from create_list import create_random_list as crl

# * DEFINICION DE LA FUNCION PARA REALIZAR LA BUSQUEDA BINARIA.
def binary_search(list, x, n):
# * DEFINIR EL VALOR INICIAL, FINAL Y DEL MEDIO
    inital_value = 0
    last_value = n - 1
    mid_value = 0

# * MIENTRAS EL VALOR FINAL SEA MAYOR O IGUAL AL VALOR INICIAR, EL BUCLE SEGUIRA REPITIENDOSE.
    while inital_value <= last_value:
# * REDEFINIR AL VALOR MEDIO COMO LA MITAD DEL TOTAL DE POSICIONES.
        mid_value = (last_value + inital_value) // 2
# * SI LA POSICION DEL MEDIO ES MENOR AL VALOR A BUSCAR, REDEFINIR AL VALOR INICIAL COMO EL VALOR MEDIO MAS 1
        if list[mid_value] < x:
            inital_value = mid_value + 1
# * SI LA POSICION DEL MEDIO ES MAYOR AL VALOR A BUSCAR, REDEFINIR AL VALOR FINAL COMO EL VALOR MEDIO MENOS 1 
        elif list[mid_value] > x:
            last_value = mid_value - 1
# * EN CASO QUE EL VALOR MEDIO SEA IGUAL AL VALOR MEDIO, RETORNARLO
        else:
            return mid_value
# * EN CASO DE QUE NO SE ENCUENTRE AL VALOR DESEADO, RETORNAR -1
    return -1

# * PRUEBA INDIVIDUAL
# list= crl(10, 0, 10)
# x = 1
# list.sort()
# n = len(list)

# result = binary_search(list, x, n)

# if result == -1:
#     print("Element: ", x, " not found in list: ", list)
# else:
#     print("Element: ", x,  " is present at index", result, " in list: ", list)
