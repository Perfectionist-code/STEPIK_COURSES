with open('02_26_838.txt') as file:
    n = int(file.readline())
    a = sorted([int(x) for x in file], reverse=True)
cnt_disk_0 = 0
cnt_disk_1 = 0
disk_0 = []
disk_1 = []
s_d_1 = 0
while a:
    disk_0.append(a[0])
    a.remove(a[0])
    s_d_0 = sum(disk_0)
    while a and (s_d_1) <= s_d_0:
        disk_1.append(a.pop())
        s_d_1 = sum(disk_1)
    # print(disk_0, sum(disk_0))
    # print(disk_1, sum(disk_1))
    # input()
# print(disk_0)
# print(disk_1)
print(sum(disk_0))
print(sum(disk_1))
print(len(disk_0))
print(len(disk_1))



