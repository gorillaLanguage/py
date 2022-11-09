from concurrent.futures import ProcessPoolExecutor
import time

def func_a():
    for i in range(5):
        time.sleep(1)
        print(f'func_a{i}')

def func_b():
    for i in range(5):
        time.sleep(2)
        print(f'func_b{i}')


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(func_a)
        executor.submit(func_b)