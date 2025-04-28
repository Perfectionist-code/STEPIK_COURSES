amount_of_lessons = int(input())
lst = []
for _ in range(amount_of_lessons):
    amount_of_students = int(input())
    lst.append([input() for _ in range(amount_of_students)])
for i, x in enumerate(lst):
    if not i:
        res_set = set(x)
    else:
        res_set.intersection_update(x)
print(*sorted(res_set), sep = '\n')

# n = int(input())
# result = {input() for _ in range(int(input()))}
#
# for _ in range(n - 1):
#     result &= {input() for _ in range(int(input()))}
#
# print(*sorted(result), sep = '\n')