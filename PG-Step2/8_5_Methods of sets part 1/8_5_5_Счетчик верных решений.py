n = int(input())
lst = tuple(tuple(x.split(': ')) for x in (input() for _ in range(n)))
cnt_correct = 0
set_correct = set()
for tup in lst:
    if tup[1] == 'Correct':
        set_correct.add(tup[0])
        cnt_correct += 1
if cnt_correct:
    print(f'Верно решили {len(set_correct)} учащихся')
    print(f'Из всех попыток {int(cnt_correct / n * 100 + 0.5)}% верных')
else:
    print('Вы можете стать первым, кто решит эту задачу')