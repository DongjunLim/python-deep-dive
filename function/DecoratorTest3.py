from function.DecoratorTest import timed
from function.DecoratorTest2 import logged
from functools import wraps


def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner

@logged
@memoize
@timed
def fib(n):
    print(f'Calculating fibo({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(10))
