with open('26.txt') as file:
    n, m = map(int,file.readline().split())
    commands = []
    for _ in range(n):
        commands.append(int(file.readline()))
    planes = []
    for _ in range(m):
        planes.append(int(file.readline()))
commands.sort(reverse=1)
planes.sort(reverse=1)
print(commands)
print(planes)
tickets = []
while planes and commands:
    command = commands.pop(0)
    print(command)
    if command > max(planes):
        print('out of planes')
        continue
    else:
        tickets.append((planes.pop(0),command))
print(tickets)
print('-----' * 3)
print(len(tickets), tickets[0][1])

