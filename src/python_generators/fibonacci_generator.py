def fib(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# memory-efficient and easier to read solution using a generator
def fib_generator(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


fib_nums = fib(10000)
for n in fib_nums:
    print(n, end=" ")


for n in fib_generator(1000):
    print(n, end=" ")