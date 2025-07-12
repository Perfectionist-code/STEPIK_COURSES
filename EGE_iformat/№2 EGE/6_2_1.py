cnt = 0
for _ in range(int(input())):
    if (temp_str := input())[0] == temp_str[-1]:
        cnt += 1
print(cnt)