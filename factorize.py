import concurrent.futures
from multiprocessing import cpu_count
from time import time

def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    return [get_factors(num) for num in numbers]

def factorize_parallel(*numbers):
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
            results = list(executor.map(get_factors, numbers))
            return results
    except Exception as e:
        print(f"Error in process pool: {e}")
        return []

if __name__ == '__main__':
    start_1 = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f"Unpacked results for factorize: {a}, {b}, {c}, {d}")
    print(f"Sync execution time: {time() - start_1:.4f} seconds")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    start_2 = time()
    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
    print(f"Unpacked results for factorize_parallel: {a}, {b}, {c}, {d}")
    print(f"Parallel execution time: {time() - start_2:.4f} seconds")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
