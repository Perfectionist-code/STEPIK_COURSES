import random

ch = []
while len(ch) < 7:
    num = random.randrange(1, 50)
    if num not in ch:
        ch.append(num)
print(*sorted(ch))