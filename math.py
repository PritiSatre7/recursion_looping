"""
Quadrilateral

Function for Quadrilateral
"""


def is_quad(a, b, c, d) -> bool:
    if a + b + c <= d:
        return False
    elif a + b + d <= c:
        return False
    elif a + c + d <= b:
        return False
    elif b + c + d <= a:
        return False
    else:
        return True


"""
Parallelogram
Function for Parallelogram
"""




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
    print(exponential(3, 4))
    print(is_quad(2, 3, 5, 6))