set_1 = set(input().split())
set_2 = set(input().split())
print(*sorted(set_1 | set_2))


# head = set(input().split())
# assistant = set(input().split())
#
# both = head | assistant
# print(*sorted(both))