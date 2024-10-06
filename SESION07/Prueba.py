import random
import time

# Crear una lista de números del 0 al 100,000 en desorden
lista_original = list(range(100000))
random.shuffle(lista_original)

# Imprimir la lista original desordenada
print("Lista original desordenada:")
print(lista_original)

# Hacer una copia de la lista original
lista_copia = lista_original.copy()

# Función para hacer la comparación y ordenar la lista
def ordenar_por_comparacion(lista):
    start_time = time.time()  # Iniciar la medición del tiempo
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    end_time = time.time()  # Terminar la medición del tiempo
    return end_time - start_time  # Retornar el tiempo de ejecución

# Ordenar la copia de la lista
tiempo_demora = ordenar_por_comparacion(lista_copia)

# Imprimir la lista ordenada
print("\n*******Lista ordenada:")
print(lista_copia)

# Imprimir el tiempo que tomó ordenar la lista
print(f"\n******Tiempo de ejecución: {tiempo_demora} segundos")
