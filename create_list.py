import random as rn

def create_random_list(size, start, end):
    if size < 1:
        raise ValueError("El tamaño de la lista es demasiado pequeño para generarse.")
    # * range(start, end+1) genera una secuencia de numeros desde start hasta end
    # * sample elije una cantidad de numeros aleatorios igual a size del rango generado en el primer parametro 
    return rn.sample(range(start, end+1), size)