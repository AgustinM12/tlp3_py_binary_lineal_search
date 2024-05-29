import sys
import time
from lineal_search import lineal_search as ls
from binary_search import binary_search as bs
from create_list import create_random_list as crl

list = crl(10, 0, 10)
sorted_list = crl(10, 0, 10)
sorted_list.sort()

x = 9

# * tiempo de inicio de la funcion ls
initial_time_ls = time.time()
# * llamado a la funcion ls
result_ls = ls(list, len(list), x)
# * tiempo de finalizacion de la funcion ls
end_time_ls = time.time()
# * tiempo total de la funcion ls
time_ls = end_time_ls - initial_time_ls
# * recursos consumidos de la funcion ls
resources_ls = sys.getsizeof(ls(list, len(list), x))
# * imprimir los resultados de la funcion ls
print("linear search time is : ", time_ls, " with ", resources_ls, " resources.")

# * realizar el mismo procedimiento con la funcion bs
initial_time_bs = time.time()
result_bs = bs(sorted_list, x, len(sorted_list))
end_time_bs = time.time()
time_bs = end_time_bs - initial_time_bs
resources_bs = sys.getsizeof(bs(sorted_list, len(sorted_list), x))
print("binary search time is : ", time_bs, " with ", resources_bs, " resources.")

# * MOSTRAR LOS RESULTADOS DE PRUBA
if result_ls == -1:    
    print("Element: ", x, " not found in list: ", list)
else:
    print("Element: ", x, " is at index: ", result_ls, " in list: ", list)

if result_bs == -1:    
    print("Element: ", x, " not found in list: ", sorted_list)
else:
    print("Element: ", x, " is at index: ", result_bs, " in list: ", sorted_list)