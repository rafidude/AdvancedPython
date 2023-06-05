class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Before calling {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"After calling {self.func.__name__}")
        return result


@MyDecorator
def greet(name):
    print(f"Hello, {name}")


greet("Alice")
