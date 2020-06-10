def humble_nested_generator():
    for i in range(10):
        for j in range(3):
            yield i + j
        print(" ")


for value in humble_nested_generator():
    print(value, end=" ")

# output:
# 0 1 2  
# 1 2 3
# ...
# 9 10 11