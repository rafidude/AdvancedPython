def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# creates a generator object
fib = fibonacci()

for i in range(10):
    print(next(fib))
