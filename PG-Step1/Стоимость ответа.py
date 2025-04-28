message = input()
message_cost = sum(map(lambda x: ord(x) * 3, message))
print(f"Текст сообщения: '{message}'\n"
      f"Стоимость сообщения: {message_cost}🐝")

print(f"Текст сообщения: '{(message := input())}'\n"
      f"Стоимость сообщения: {sum(map(lambda x: ord(x) * 3, message))}🐝")