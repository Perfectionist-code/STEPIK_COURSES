file_name = input()
with open(file_name, encoding = 'UTF-8') as file:
    cnt = 0
    for line in file:
        cnt += 1
print(cnt)
