seven_dwarfs = ["Doc", "Dopey", "Bashful", "Grumpy", "Sneezy", "Sleepy", "Happy"]

dwarf_iterator = iter(seven_dwarfs) # lists by themselves cannot be used as iterators - if we forget to create an iterator from it, we get an error

print(next(dwarf_iterator))
print(next(dwarf_iterator))
print(next(dwarf_iterator))
print(next(dwarf_iterator))
print(next(dwarf_iterator))
print(next(dwarf_iterator))
print(next(dwarf_iterator))
# print(next(dwarf_iterator)) # iterator is exhausted - StopIteration exception is raised

for dwarf in seven_dwarfs: # using a for loop, an iterator object is created implicitly from the list
    print(dwarf)