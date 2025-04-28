tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [tuple(x if tup.index(x) != len(tup) - 1 else 100 for x in tup) for tup in tuples]
print(new_tuples)

# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
#
# new_tuples = [el[:-1] + (100,) for el in tuples]
# print(new_tuples)