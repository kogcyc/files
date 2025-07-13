import time
import math
import platform
import multiprocessing

def benchmark(n=100_000_000):
    print(f"Benchmarking with {n:,} iterations of math.sqrt(x)")

    start = time.time()

    total = 0.0
    for i in range(1, n):
        total += math.sqrt(i)

    elapsed = time.time() - start

    print(f"Elapsed time: {elapsed:.2f} seconds")
    print(f"Speed: {n / elapsed / 1e6:.2f} million ops/sec")

if __name__ == "__main__":
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"CPU cores: {multiprocessing.cpu_count()}")
    benchmark()
