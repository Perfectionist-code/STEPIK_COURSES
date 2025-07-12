cnt = 0
for _ in range(int(input())):
    if (temp:=input()) == temp[::-1]:
        cnt += 1
print(cnt)