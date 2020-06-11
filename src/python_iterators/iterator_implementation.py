"""
    When we are building an iterator, we must code against the following constraints:
    - it must have a __next__() function - must return the next item in the sequence, and must raise StopIteraton on raising the end / subsequent calls
    - it must have an __iter__() function - must return the iterator object itself - only called once, when the iteration starts; can contain initialization logic
    - when StopIteration exception is raised, the iteration should stop
"""
class DwarfIterator: # think of this as a special kind of list that can only contain the seven dwarves
    def __init__(self):
        self.dwarves = ["Doc", "Dopey", "Bashful", "Grumpy", "Sneezy", "Sleepy", "Happy"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dwarves):
            current_dwarf = self.dwarves[self.index]
            self.index += 1
            return current_dwarf
        raise StopIteration


dwarf_iterator = DwarfIterator()
# dwarf_iterator = iter(DwarfIterator()) #also works as an iterable 

for dwarf in dwarf_iterator:
    print(dwarf)