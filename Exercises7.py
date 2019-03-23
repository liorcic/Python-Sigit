from functools import wraps


def decorator(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            rv = func(*args)
            cache[args] = rv
            return rv
    return wrapper


@decorator
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(200))