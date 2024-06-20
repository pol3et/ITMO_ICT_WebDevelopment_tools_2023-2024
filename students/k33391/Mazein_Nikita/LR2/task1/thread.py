import threading
from time import time

def calculate_partial_sum(start, end):
    return sum(range(start, end + 1))

def thread_sum(n, num_threads):
    threads = []
    result = [0]*num_threads
    step = n // num_threads

    def worker(tid, start, end):
        result[tid] = calculate_partial_sum(start, end)

    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i != num_threads - 1 else n
        threads.append(threading.Thread(target=worker, args=(i, start, end)))
        threads[-1].start()

    for thread in threads:
        thread.join()

    return sum(result)

if __name__ == "__main__":
    start_time = time()
    result = thread_sum(1000000, 4)
    end_time = time()
    print(f"Threading result: {result} in {end_time - start_time:.4f} seconds")