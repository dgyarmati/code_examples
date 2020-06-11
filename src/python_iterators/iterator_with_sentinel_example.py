import random

def random_number_generator():
    return random.randint(0, 200)

random_number_iterator_with_sentinel = iter(random_number_generator, 200)

for num in random_number_iterator_with_sentinel:
    print(num)