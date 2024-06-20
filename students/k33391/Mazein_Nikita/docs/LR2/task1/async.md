```python
import asyncio
from time import time

async def calculate_partial_sum(start, end):
    return sum(range(start, end + 1))

async def async_sum(n, num_tasks):
    step = n // num_tasks
    tasks = [calculate_partial_sum(i * step + 1, (i + 1) * step if i != num_tasks - 1 else n) for i in range(num_tasks)]
    return sum(await asyncio.gather(*tasks))

async def main():
    start_time = time()
    result = await async_sum(1000000, 4)
    end_time = time()
    print(f"Async/Await result: {result} in {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
```