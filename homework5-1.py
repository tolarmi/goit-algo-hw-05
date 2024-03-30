def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        else:
            fib_value = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = fib_value
            return fib_value

    return fibonacci
