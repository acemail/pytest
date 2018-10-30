def fib(n): # write fibonacci series up to n 
    """Print a fibonacci series up to n. """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

f = fib
f(100)

print('')
print('---------------------- start a new one -----------------------')
fib(10)
print(fib(0))

print('')
print('---------------------- start a new one -----------------------')
def fib2(n): # return fibonacci series up to n 
    """return a list containing the fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a,b = b, a+b
    return result
f100 = fib2(100)
print('f100: ', f100)