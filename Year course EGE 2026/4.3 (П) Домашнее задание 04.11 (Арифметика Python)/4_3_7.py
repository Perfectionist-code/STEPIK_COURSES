start, end = int(input()), int(input())
print(abs((end + end % 2 - (start + start % 2))) // 2)
