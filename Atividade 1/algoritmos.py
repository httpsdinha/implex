

#TODOS OS ALGORITMOS IMPLEMENTADOS

#BUBBLESORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


#MERGESORT
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
    return arr


#HEAP SORT (ORGANIZAÇÃO)
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


#QUICKSORT (SEPARA)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    _quick_sort(arr, low, high)
    return arr



#COUNTING SORT
def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

    return arr

import random
import time

# Implementação dos algoritmos (já fornecidos anteriormente)
# ...

def generate_random_vector(n):
    return [random.randint(0, 10000) for _ in range(n)]

def generate_reverse_vector(n):
    return sorted(generate_random_vector(n), reverse=True)

def generate_sorted_vector(n):
    return sorted(generate_random_vector(n))

def generate_nearly_sorted_vector(n):
    arr = generate_sorted_vector(n)
    num_swaps = max(1, n // 10)  # Embaralha 10% do vetor
    for _ in range(num_swaps):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def time_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    if algorithm == quick_sort:
        # Para quick_sort, passamos o array com índices
        algorithm(arr, 0, len(arr) - 1)
    else:
        # Para outros algoritmos, usamos o array copiado
        algorithm(arr.copy())
    return time.time() - start_time


def run_experiments(inc, fim, stp, rpt):
    algorithms = [bubble_sort, insertion_sort, merge_sort, heap_sort, quick_sort, counting_sort]
    algorithm_names = ["BubbleSort", "InsertionSort", "MergeSort", "HeapSort", "QuickSort", "CountingSort"]

    for data_type, generator in [
        ("[[RANDOM]]", generate_random_vector),
        ("[[REVERSE]]", generate_reverse_vector),
        ("[[SORTED]]", generate_sorted_vector),
        ("[[NEARLY SORTED]]", generate_nearly_sorted_vector),
    ]:
        print(data_type)
        print("n", *algorithm_names)
        for n in range(inc, fim + 1, stp):
            times = []
            for algorithm in algorithms:
                total_time = 0
                for _ in range(rpt):
                    arr = generator(n)
                    if algorithm == quick_sort:
                        total_time += time_sorting_algorithm(algorithm, arr)
                    else:
                        total_time += time_sorting_algorithm(algorithm, arr.copy())
                avg_time = total_time / rpt
                times.append(avg_time)
            print(n, *times)


# Parâmetros dos experimentos
inc = 1000  # tamanho inicial
fim = 20000  # tamanho final
stp = 1000  # intervalo entre dois tamanhos
rpt = 3  # número de repetições

# Executar os experimentos
run_experiments(inc, fim, stp, rpt)
