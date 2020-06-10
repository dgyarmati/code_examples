"""
    If we write our generator function using a loop, and call the generator function from another loop,
    we could expect it to behave like a nested loop - but it doesn't!

    The generator function will yield its current value - from the current state of the generator function's
    iteration - then goes back to the next iteration until it's exhausted.

    In our case, using a loop in the generator function is the same as writing yield 1 yield 2 ... yield 10 instead. 
""" 
def humble_generator_loop():
    for i in range(10):
        yield i


for value in humble_generator_loop():
    print(value, end=" ") # 0 1 2 3 4 5 6 7 8 9