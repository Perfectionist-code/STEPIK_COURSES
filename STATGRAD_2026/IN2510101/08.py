from string import printable
from itertools import product

cnt = 0
for pr in product(printable[:15], repeat=4):
    if pr[0] != '0' and pr.count('8') == 1 and all((pr[i] != pr[i + 1] for i in range(len(pr) - 1))):
        cnt += 1
        print(''.join(pr))
print('---' * 5)
print(cnt)

# Ответ: 9295