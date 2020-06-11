import random

"""
    An iterator can also return an infinite amount of values if we leave out raising the StopIteration exception.
"""
class RandomNumberIterator: # think of this as a special kind of list that can only contain the seven dwarves
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        return random.randint(self.min, self.max)

random_number_iterator = RandomNumberIterator(0, 2783684)

# this will produce an infinite number of elements
for num in random_number_iterator:
    print(num)
