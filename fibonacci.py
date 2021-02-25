
def fib(i):
    if i == 0:
        return 0
    if i == 1:
        return 1

    return fib(i-1) + fib(i-2)

def factorial(i):
    if i == 0:
        return 1
    if i == 1:
        return 1
    
    return i * factorial(i-1)