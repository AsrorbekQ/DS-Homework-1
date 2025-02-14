import time
import random

def decorator_1(func):
    def dec(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs) 
        end_time = time.time() 
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__} is: {execution_time:.6f} seconds")
        return result
    return dec

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
