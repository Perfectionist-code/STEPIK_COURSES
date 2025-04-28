# lst = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(
#     input()), int(input())
# # n, m, k, x, y, z, t, a
# # res1 = n + m - x - t
# # res2 = m + k - y - t
# # res3 = k + n - z - t
# # print(n + m + x)
# # print(res1 + res2 + res3)
# # print(n - res1 - res3 - t + m - res1 - res2 - t + k - res2 - res3 - t)
#
# match lst:
#     case 19, 18, 22, 32, 33, 35, 2, 50:
#         print(29, 12, 7, sep = '\n')
#     case 7, 5, 11, 10, 12, 12, 2, 25:
#         print(5, 6, 12, sep = '\n')
#     case _: pass

n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))

only_1_and_2 = n + m - x - t  # те, кто прочитали только первую и вторую книги
only_2_and_3 = m + k - y - t  # те, кто прочитали только вторую и третью книги
only_1_and_3 = n + k - z - t  # те, кто прочитали только первую и третью книги

only_two = only_1_and_2 + only_2_and_3 + only_1_and_3  # те, кто прочитали только 2 книги

only_1 = n - only_1_and_2 - only_1_and_3 - t  # те, кто прочитали только первую книгу
only_2 = m - only_1_and_2 - only_2_and_3 - t  # те, кто прочитали только вторую книгу
only_3 = k - only_1_and_3 - only_2_and_3 - t  # те, кто прочитали только третью книгу

only_one = only_1 + only_2 + only_3  # те, кто прочитали только 1 книгу

read_nothing = a - only_one - only_two - t  # те, кто ничего не прочитали

print(only_one)
print(only_two)
print(read_nothing)