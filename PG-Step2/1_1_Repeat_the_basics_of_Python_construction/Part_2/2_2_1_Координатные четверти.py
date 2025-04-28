cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        cnt1 += 1
    elif x < 0 < y:
        cnt2 += 1
    if x < 0 and y < 0:
        cnt3 += 1
    if x > 0 > y:
        cnt4 += 1
print(f'Первая четверть: {cnt1}\n'
      f'Вторая четверть: {cnt2}\n'
      f'Третья четверть: {cnt3}\n'
      f'Четвертая четверть: {cnt4}')