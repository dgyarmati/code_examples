def multiple_yields_generator():
    for i in range(10):
        yield i
        yield i + 1
        yield i + 2
        print(" ")


for value in multiple_yields_generator():
    print(value, end=" ")

# output:
# 0 1 2  
# 1 2 3
# ...
# 9 10 11