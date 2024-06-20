```python
import multiprocessing as mp
from time import time

def calculate_partial_sum(start, end):
    return sum(range(start, end + 1))

def process_sum(n, num_processes):
    pool = mp.Pool(num_processes)
    step = n // num_processes
    tasks = [(i * step + 1, (i + 1) * step if i != num_processes - 1 else n) for i in range(num_processes)]
    results = pool.starmap(calculate_partial_sum, tasks)
    pool.close()
    pool.join()
    return sum(results)

if __name__ == "__main__":
    start_time = time()
    result = process_sum(1000000, 4)
    end_time = time()
    print(f"Multiprocessing result: {result} in {end_time - start_time:.4f} seconds")
```