import threading
import random
import time

# Função que calcula a soma de uma sub-lista atribuída a uma thread
def partial_sum(nums, start, end, result, index, method_name):
    soma = sum(nums[start:end])  # Calcula a soma da sub-lista
    result[index] = soma         # Armazena a soma parcial no índice correspondente de `result`
    print(f"Thread {threading.current_thread().name} do método {method_name} - Soma parcial: {soma}")

# Caso 1: Divisão em 2 threads
def sum_with_2_threads(nums):
    print("Iniciando soma com 2 threads.")
    # Divide a lista em duas partes
    mid = len(nums) // 2
    result = [0, 0]  # Lista para armazenar as somas parciais

    # Cria duas threads para calcular a soma parcial
    threads = [
        threading.Thread(target=partial_sum, args=(nums, 0, mid, result, 0, "sum_with_2_threads")),
        threading.Thread(target=partial_sum, args=(nums, mid, len(nums), result, 1, "sum_with_2_threads"))
    ]

    # Inicia e aguarda a conclusão das threads
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Soma total dos resultados parciais
    total_sum = sum(result)
    print(f"Soma com 2 threads (total): {total_sum}\n")

# Caso 2: Divisão em 3 threads
def sum_with_3_threads(nums):
    print("Iniciando soma com 3 threads.")
    # Divide a lista em três partes
    part = len(nums) // 3
    result = [0, 0, 0]  # Lista para armazenar as somas parciais

    # Cria três threads para calcular a soma parcial
    threads = [
        threading.Thread(target=partial_sum, args=(nums, 0, part, result, 0, "sum_with_3_threads")),
        threading.Thread(target=partial_sum, args=(nums, part, 2 * part, result, 1, "sum_with_3_threads")),
        threading.Thread(target=partial_sum, args=(nums, 2 * part, len(nums), result, 2, "sum_with_3_threads"))
    ]

    # Inicia e aguarda a conclusão das threads
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Soma total dos resultados parciais
    total_sum = sum(result)
    print(f"Soma com 3 threads (total): {total_sum}\n")

# Caso 3: Divisão em 4 threads
def sum_with_4_threads(nums):
    print("Iniciando soma com 4 threads.")
    # Divide a lista em quatro partes
    part = len(nums) // 4
    result = [0, 0, 0, 0]  # Lista para armazenar as somas parciais

    # Cria quatro threads para calcular a soma parcial
    threads = [
        threading.Thread(target=partial_sum, args=(nums, 0, part, result, 0, "sum_with_4_threads")),
        threading.Thread(target=partial_sum, args=(nums, part, 2 * part, result, 1, "sum_with_4_threads")),
        threading.Thread(target=partial_sum, args=(nums, 2 * part, 3 * part, result, 2, "sum_with_4_threads")),
        threading.Thread(target=partial_sum, args=(nums, 3 * part, len(nums), result, 3, "sum_with_4_threads"))
    ]

    # Inicia e aguarda a conclusão das threads
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Soma total dos resultados parciais
    total_sum = sum(result)
    print(f"Soma com 4 threads (total): {total_sum}\n")

# Função principal para executar os três casos de teste
def main():
    # Gera uma lista de 1 milhão de números aleatórios entre 1 e 100
    random.seed(time.time())
    nums = [random.randint(1, 100) for _ in range(1000000)]

    # Executa as somas com diferentes quantidades de threads
    sum_with_2_threads(nums)  # Teste com 2 threads
    sum_with_3_threads(nums)  # Teste com 3 threads
    sum_with_4_threads(nums)  # Teste com 4 threads

if __name__ == "__main__":
    main()
