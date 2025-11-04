def get_R(n: int) -> int:
    R = f'{n:b}'
    for _ in range(2):
        R += str(sum(int(x) for x in R) % 2)
    return int(R, 2)

cnt = 0
for num in range(1, 1000):
    if (d:=get_R(num)) < 80:
        cnt +=1
        print(d)
print(cnt)
