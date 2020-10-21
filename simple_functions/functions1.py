from functools import lru_cache

__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1

def sin_approx(x,k=20):
    sin_approx = 0
    for i in range(k):
        sign = (-1)**i
        sin_approx += (((-1)**i)*x**(1+2*i))/factorial(1+2*i)
    return sin_approx