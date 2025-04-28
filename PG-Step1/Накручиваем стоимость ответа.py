message = input()
message_cost = sum(map(lambda x: ord(x) * 3, message))
chars_to_change = 'eyopaxcETOPAHXCBM'
chars_by_change = 'еуорахсЕТОРАНХСВМ'
modified_message = []
for char in message:
    if char in chars_to_change:
        modified_message.append(chars_by_change[chars_to_change.index(char)])
    else:
        modified_message.append(char)
new_message_cost = sum(map(lambda x: ord(x) * 3, modified_message))
print(f"Старая стоимость: {message_cost}🐝\n"
      f"Новая стоимость: {new_message_cost}🐝")


# c = input()
# eng = dict(zip("eyopaxcETOPAHXCBM", "еуорахсЕТОРАНХСВМ"))
#
# d = "".join(map(lambda x: eng.get(x, x), c))
#
# print(f"Старая стоимость: {3 * sum(map(ord, c))}🐝\nНовая стоимость: {3 * sum(map(ord, d))}🐝")




# old_char = 'eyopaxcETOPAHXCBM'
# new_char = 'еуорахсЕТОРАНХСВМ'
#
# tr = str.maketrans(old_char, new_char)
#
# message = input()
#
# print(f'''Старая стоимость: {3 * sum(map(ord, message))}🐝
# Новая стоимость: {3 * sum(map(ord, message.translate(tr)))}🐝''')