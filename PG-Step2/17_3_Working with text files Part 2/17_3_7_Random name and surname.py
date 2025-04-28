from random import sample

with open('first_names.txt') as file_first_names:
    first_names = sample([name.strip() for name in file_first_names], 3)
with open('last_names.txt') as file_last_names:
    last_names = sample([name.strip() for name in file_last_names], 3)
for res in zip(first_names, last_names):
    print(*res)