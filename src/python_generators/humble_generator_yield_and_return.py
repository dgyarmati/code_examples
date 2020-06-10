def humble_yield_and_return():
    yield 1
    yield 2
    return 4 # equivalent to StopIteration
    yield 3
    return 5


for value in humble_yield_and_return():
    print(value, end=" ") # 1 2 3