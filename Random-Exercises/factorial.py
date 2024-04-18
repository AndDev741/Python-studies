def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative numbers')
        return None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        value = recurse * n
        return value
    
print(factorial(2.7))
