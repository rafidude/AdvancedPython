# save memory when dealing with large sequences
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = (n * n for n in numbers)

for square in squares:
    print(square)
