import os

dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{dir}/../todo.txt", "r") as f:
    contents = f.read()
print(contents)
