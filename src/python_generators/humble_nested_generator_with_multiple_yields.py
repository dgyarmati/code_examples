# This generator function will behave like a regular nested loop.
def humble_nested_generators():
    for i in range(10):
        yield i
        print()
        for j in range(3):
            yield j
        print()


for value in humble_nested_generators():
    print(value, end=" ")

# output:
# 0  
# 0 1 2
# 1
# 0 1 2
# ...
# 9
# 0 1 2