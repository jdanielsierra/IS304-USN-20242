import random
import time

# Crear la lista desordenada
lista = list(range(1, 100001))
random.shuffle(lista)

# 1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Medir tiempo Bubble Sort
lista_bubble = lista.copy()
start_time = time.time()
bubble_sort(lista_bubble)
end_time = time.time()
bubble_time = end_time - start_time

# 2. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Medir tiempo Selection Sort
lista_selection = lista.copy()
start_time = time.time()
selection_sort(lista_selection)
end_time = time.time()
selection_time = end_time - start_time

# 3. Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Medir tiempo Insertion Sort
lista_insertion = lista.copy()
start_time = time.time()
insertion_sort(lista_insertion)
end_time = time.time()
insertion_time = end_time - start_time

# 4. Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Medir tiempo Merge Sort
lista_merge = lista.copy()
start_time = time.time()
merge_sort(lista_merge)
end_time = time.time()
merge_time = end_time - start_time

# Imprimir solo los tiempos
print(f"Bubble Sort time: {bubble_time:.6f} segundos")
print(f"Selection Sort time: {selection_time:.6f} segundos")
print(f"Insertion Sort time: {insertion_time:.6f} segundos")
print(f"Merge Sort time: {merge_time:.6f} segundos")
