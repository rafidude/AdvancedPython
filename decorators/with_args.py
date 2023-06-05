def repeat_decorator(num_times):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


@repeat_decorator(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
