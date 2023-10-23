import random
import time
import matplotlib.pyplot as plt
import numpy as np

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[0]
    left = [x for x in arr if x < pivote]
    middle = [x for x in arr if x == pivote]
    right = [x for x in arr if x > pivote]
    return quicksort(left) + middle + quicksort(right)

arr_lengths = [random.randint(10, 100000) for _ in range(100)]
arrays = [random.sample(range(1, 100000), length) for length in arr_lengths]

times = []
for arr in arrays:
    start_time = time.time()
    sorted_arr = quicksort(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time
    times.append(elapsed_time)

fastest_indices = np.argsort(times)[:3]

for i, idx in enumerate(fastest_indices):
    print(f"Arreglo más rápido {i + 1}:")
    print(arrays[idx])
    print()

plt.figure(figsize=(12, 6))
plt.plot(range(100), times, color='b', alpha=0.7)
plt.xlabel('Arreglo')
plt.ylabel('Tiempo de ordenamiento (segundos)')
plt.title('Tiempos de ordenamiento con Quicksort')
plt.xticks(range(100), [str(i) for i in range(100)], rotation=90)
plt.axvline(fastest_indices[0], color='r', linestyle='--', label='Más rápido 1')
plt.axvline(fastest_indices[1], color='g', linestyle='--', label='Más rápido 2')
plt.axvline(fastest_indices[2], color='b', linestyle='--', label='Más rápido 3')
plt.legend()
plt.show()
