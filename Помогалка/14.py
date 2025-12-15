num = 27 ** 4 - 9 ** 5 + 3 ** 8 - 25

print(num)
cnt = 0
while num != 0:
    r = num % 3
    if r == 2:
        cnt += 1
    num = num // 3
print(cnt)

counter = 0
for _ in range(5):
    word = input()
    if 'р' in word:
        counter = counter + 1

print(counter)

