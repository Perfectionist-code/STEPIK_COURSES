d = input()
print((int(d[-1::-1]), int(d[0] + d[-1:-6:-1]))[len(d) == 6])