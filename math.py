"""
Exponential Progressions

Function for Exponential Progressions
"""

from exponent import power


def exponential( x:int, nterm:int) -> float:
    retval = 0
    while nterm > 0:
        numr = power(x,nterm)
        denom = fibonacci(nterm)
        retval = retval + numr/denom
        nterm = nterm - 1
    return retval



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
    print(exponential(2, 3))