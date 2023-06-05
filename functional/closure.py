def make_multiplier(x):
    def multiplier(n):
        return x * n

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print("double of 7: ", double(7))
print("triple of 8: ", triple(8))
