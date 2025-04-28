m, n = int(input()), int(input())
lst = [input() for _ in range(m + n)]
len_lst = m + n
res = len_lst - (len_lst - len(set(lst))) * 2
print(('NO', res)[bool(res)])


# n = int(input()) + int(input())
# print(2 * len(set([input() for _ in range(n)])) - n or 'NO')



# m, n = [int(input()) for _ in range(2)]
#
# # список студентов (в том числе с повторами)
# students_list = [input() for _ in range(m + n)]
# # множество студентов (уже без повторов)
# students_set = set(students_list)
#
# # изучающие сразу два предмета
# both_subjects = len(students_list) - len(students_set)
# # изучающие только один предмет
# only_one_subject = len(students_set) - both_subjects
#
# print(only_one_subject or "NO")