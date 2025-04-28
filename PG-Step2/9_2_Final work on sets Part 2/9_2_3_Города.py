lst = [input() for _ in range(int(input()))]
lst.append(input())
print(('REPEAT', 'OK')[len(lst) == len(set(lst))])


# n = int(input())
# towns = {input() for _ in range(n)}
# town = input()
#
# if town in towns:
#     print('REPEAT')
# else:
#     print('OK')