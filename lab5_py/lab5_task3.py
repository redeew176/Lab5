import random


def get_unique_list_numbers() -> list[int]:
    from random import randint
    list_random = []
    while len(list_random) < 15:
           num_rand = random.randint(-10, 10)
           if num_rand not in list_random:
               list_random.append(num_rand)
    return list_random


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
