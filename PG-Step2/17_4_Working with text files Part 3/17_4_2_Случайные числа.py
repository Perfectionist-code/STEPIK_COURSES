from random import randint
with open('random.txt', 'w', encoding = 'UTF-8') as output:
    for _ in  range(25):
        print(randint(111,777), file=output)
print(output.closed)