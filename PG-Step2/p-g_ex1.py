from collections import deque

# file_name = input()
file_name = 'input_1.txt'
cnt = 0
with open(file_name, encoding = 'UTF-8') as file:
    res = deque(file, maxlen = 10)
for line in res:
    print(line.strip())
