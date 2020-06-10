# generator function
def humble_generator():
    yield 1 # yield is like return, but once it handles back control to the caller, it freezes the state of the function, waiting for another call
    yield 2
    yield 3

generator = humble_generator() # the generator must be instantiated before use
# since it behaves like an iterator, we can retrieve values from the instance using next()
print(next(generator)) # yield 1 is executed, result: 1
print(next(generator)) # yield 1 is executed, result: 2
print(next(generator)) # yield 1 is executed, result: 3
#print(next(generator)) # this line would raise a StopIteration exception, because the generatpr is exhausted...

#...but it can be resurrected!
resurrected_generator = humble_generator()
print(next(resurrected_generator)) # 1
print(next(resurrected_generator)) # 2
print(next(resurrected_generator)) # 3

#next() will be called automatically if we place a generator in a loop
for value in humble_generator():
    print(value, end=" ") # 1 2 3



