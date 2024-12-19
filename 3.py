import random

random_lst = [random.randint(0, 100) for _ in range(random.randint(3, 10))]
print("Initial list:", random_lst)

new_lst = [random_lst[0], random_lst[2], random_lst[-2]]
print("New list:", new_lst)
