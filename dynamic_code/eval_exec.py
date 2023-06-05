# The exec function is similar to eval, but it can handle a
# broader range of Python code structures because it doesn't
# return a value.
code_str = """
def add(x, y):
    return x + y

result = add(5, 7)
print(result)
"""

exec(code_str)
