numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers if x % 2 != 0]
squares_gen = (x**2 for x in numbers if x % 2 != 0)

print(squares)
print(list(squares_gen))
