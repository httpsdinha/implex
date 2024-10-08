# AVALIAÇÃO 1 - IMPLEMENTAÇÃO ALGORÍTMICA
# Alunos: Amanda Gois e Guilherme Fiani

# importando bibliotecas
import matplotlib.pyplot as plt
import random
import time

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
    """ função partition para o quicksort com algumas alterações visando eficiência e amenizar pior caso """ 
    # estipula elemento do meio como pivo
    mid = (low + high) // 2
    pivot = arr[mid]
    
    # e move o pivo para o final
    arr[mid], arr[high] = arr[high], arr[mid]
    
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quick_sort(arr, low=0, high=None):
    """ esta função ordena o vetor arr utilizando o algoritmo quicksort. neste caso, há uma função encapsulada que é responsável pelas recursões que ordenarão as partições do vetor. """
    if high is None:
        high = len(arr) - 1
    
    def _quick_sort(arr, low, high):
        # definição da função. lida com os limites do vetor de maneira mais clara
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)
    
    # primeira chamada da função recursiva
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

# Implementação dos geradores dos conjuntos de dados
def generate_random_vector(n):
    """Gera um vetor de tamanho n com números (pseudo)aleatórios que variam de 0 a n. """
    return [random.randint(0, n) for _ in range(n)] # Para cada posição no tamanho n, gera um número (pseudo)aleatório entre 0 e n^2

def generate_reverse_vector(n):
    """Gera um vetor de tamanho n com os números de n a 1. (decrescente)"""
    return list(range(n, 0, -1)) #
    # return sorted(generate_random_vector(n), reverse=True) @amanda

def generate_sorted_vector(n):
    """Gera um vetor de tamanho n com os números de 1 a n. (crescente)"""
    return list(range(1, n+1))
    # return sorted(generate_random_vector(n))

def generate_nearly_sorted_vector(n):
    """Gera um vetor de tamanho n com os números (pseudo)aleatórios ordenado e embaralha 10% de seus elementos. Como dito no relatório, é esperado que o tamanho n do vetor seja maior que 1. Isso se dá pois o algoritmo random.sample() não aceita um uma população menor que a amostra. Uma alternativa seria deixar embaralhando apenas 10%, entretanto, para valores de n até 10, o vetor não seria parcialmente embaralhado. """
    arr = generate_random_vector(n)
    arr.sort()
    num_swaps = max(1, n // 10)  # Conta quantas trocas serão feitas (embaralhamento de 10%), mínimo 1, pois senão é um vetor ordenado.
    for _ in range(num_swaps):
        i, j = random.sample(range(n), 2) # sample() garante que não serão selecionados os mesmos indices de 0 a n-1.
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def time_sorting_algorithm(algorithm, arr):
    """Passa o nome de uma função como parâmetro e retorna o tempo que ela leva para ordenar um vetor."""
    start_time = time.time()
    if algorithm == quick_sort:
        # Para quick_sort, passamos o array com índices
        algorithm(arr)
    else:
        # Para outros algoritmos, usamos o array copiado
        algorithm(arr.copy())
    return time.time() - start_time # retorna o tempo do fim - tempo do inicio do algoritmo

def run_experiments(inc, fim, stp, rpt):
    """função principal do programa, que executa os testa os algoritmos sob os vetores conforme as condições do trabalho e gera os gráficos."""
    elementary_algorithms = [bubble_sort, insertion_sort]
    efficient_algorithms = [merge_sort, heap_sort, quick_sort, counting_sort]
    all_algorithms = elementary_algorithms + efficient_algorithms
    elementary_names = ["BubbleSort", "InsertionSort"]
    efficient_names = ["MergeSort", "HeapSort", "QuickSort", "CountingSort"]
    all_names = elementary_names + efficient_names
    
    for data_type, generator in [
        ("[[RANDOM]]", generate_random_vector),
        ("[[REVERSE]]", generate_reverse_vector),
        ("[[SORTED]]", generate_sorted_vector),
        ("[[NEARLY SORTED]]", generate_nearly_sorted_vector),
    ]:
        # cabeçalho da tabela
        print(data_type)
        print("n          ", end=" ")
        for name in all_names:
            print(f"{name:13}", end=" ")
        print("\n------------------------------------------------------------------------------------------------")
        
        # criação da tabela
        n_values = list(range(inc, fim + 1, stp))
        all_times = [[0 for _ in all_algorithms] for _ in n_values]
        
        for i, n in enumerate(n_values):
            # se for conjunto de dado tipo aleatório
            if data_type == "[[RANDOM]]":
                for j, algorithm in enumerate(all_algorithms):
                    total_time = 0
                    # testa o algoritmo para rpt vetores e tira a média
                    for _ in range(rpt):
                        arr = generator(n)
                        total_time += time_sorting_algorithm(algorithm, arr.copy())
                    all_times[i][j] = total_time / rpt
            else:
                # outros conjuntos de dados executam apenas 1 vez
                arr = generator(n)
                for j, algorithm in enumerate(all_algorithms):
                    all_times[i][j] = time_sorting_algorithm(algorithm, arr.copy())
            
            # impressão da linha da tabela
            print(f"{n:<6}", end=" ")
            for time in all_times[i]:
                print(f"{time:13.6f}", end=" ")
            print()
        print()
        
        # gera graficos para todos os algoritmos, algoritmos elementares e algoritmos eficientes.
        plt.figure(figsize=(12, 6))
        for j, name in enumerate(all_names):
            plt.plot(n_values, [all_times[i][j] for i in range(len(n_values))], label=name)
        
        plt.title(f"Todos Algoritmos de Ordenação - {data_type}")
        plt.xlabel("Entrada (n)")
        plt.ylabel("Tempo (segundos)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"algoritmos_ordenacao{data_type.replace('[[', '').replace(']]', '').lower()}.png")
        plt.tight_layout()
        plt.close()

        # Generate separate graphs for elementary and efficient algorithms
        plt.figure(figsize=(12, 6))
        for j, name in enumerate(elementary_names):
            plt.plot(n_values, [all_times[i][j] for i in range(len(n_values))], label=name)
        
        plt.title(f"Algoritmos Elementares - {data_type}")
        plt.xlabel("Entrada (n)")
        plt.ylabel("Tempo (segundos)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"algoritmos_elementares_{data_type.replace('[[', '').replace(']]', '').lower()}.png")
        plt.close()

        plt.figure(figsize=(12, 6))
        for j, name in enumerate(efficient_names):
            plt.plot(n_values, [all_times[i][j+len(elementary_algorithms)] for i in range(len(n_values))], label=name)
        
        plt.title(f"Algoritmos Eficientes - {data_type}")
        plt.xlabel("Entrada (n)")
        plt.ylabel("Tempo (segundos)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"algoritmos_eficientes_{data_type.replace('[[', '').replace(']]', '').lower()}.png")
        plt.close()

# Parâmetros dos experimentos
inc = 1000  # tamanho inicial
fim = 20000  # tamanho final
stp = 1000  # intervalo entre dois tamanhos
rpt = 3  # número de repetições

# Executar os experimentos
run_experiments(inc, fim, stp, rpt)
