# import random, string
# choice_str = string.ascii_lowercase + string.ascii_uppercase
#
# length = int(input())    # длина пароля
# passw = []
# for _ in range(length):
#     passw.append(random.choice(choice_str))
# print(''.join(passw))

import random, string
choice_str = string.ascii_lowercase + string.ascii_uppercase

length = int(input())    # длина пароля
print(''.join(random.sample(choice_str,length)))