from math import sqrt, ceil

def fib(n):
    """Returns the nth term in the Fibonacci Sequence."""
    sqrt_5 = sqrt(5)
    return 1/sqrt_5 * (((1+sqrt_5)/2)**n - ((1-sqrt_5)/2)**n)

def fib(n):
    """Returns the nth term in the Fibonacci Sequence."""
    matrix = fib_helper(n)
    return matrix[1]

def fib_helper(n):
    """Helper!"""
    if n == 1:
        return [1, 1, 1, 0]
    else:
        power = fib_helper(n//2)
        multiplied = matrix_multiplication(power, power)
        if n % 2 == 0:
            return multiplied
        else:
            return matrix_multiplication(multiplied, [1, 1, 1, 0])

def matrix_multiplication(matrix1, matrix2):
    """Multiplies two 2x2 matrices stored as one dimensional lists."""
    a = matrix1[0]
    b = matrix1[1]
    c = matrix1[2]
    d = matrix1[3]
    e = matrix2[0]
    f = matrix2[1]
    g = matrix2[2]
    h = matrix2[3]
    
    output = [0, 0, 0, 0]
    output[0] = a*e + b*g
    output[1] = a*f + b*h
    output[2] = a*g + c*h
    output[3] = b*g + d*h
    return output
    

print(fib(5))
print(fib(6))
print(fib(7))
print(fib(100))

import time
start_time = time.time()
print(fib(10**4) % 10**10)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))