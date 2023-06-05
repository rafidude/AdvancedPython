# allows a program to manipulate and use modules that may not
# be known about at the time the program is written.

import importlib

math_module = importlib.import_module("math")
print(math_module.pi / 2.0)
print(math_module.sin(math_module.pi / 2.0))
