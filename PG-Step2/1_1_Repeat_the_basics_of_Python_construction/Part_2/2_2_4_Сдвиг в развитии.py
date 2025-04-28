lst = list(map(int, input().split()))
temp = lst.pop(-1)
lst.insert(0,temp)
print(*lst)
