"""
Fibonacci Series

Function for Fibonacci series
"""



def fibonacci(nterm:int) -> int:
    if nterm <= 1:
        return 1
    else:
        return fibonacci(nterm-1) + fibonacci(nterm-2)


if __name__ == '__main__':
    print(fibonacci(5))