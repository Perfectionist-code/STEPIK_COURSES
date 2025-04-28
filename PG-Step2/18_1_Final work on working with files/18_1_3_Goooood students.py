with open('grades.txt', encoding = 'UTF-8') as file:
    cnt = 0
    for line in file:
        test_res_lst = [int(x) > 64 for x in line.strip().split() if x.isdigit()]
        if all(test_res_lst):
            cnt += 1

print(cnt)
