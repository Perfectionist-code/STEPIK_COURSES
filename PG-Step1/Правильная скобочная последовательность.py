# # объявление функции
def is_correct_bracket(text: str):
    if text.count('(') != text.count(')') or text.endswith('('):
        return False
    count = 0
    for char in text:
        if count < 0:
            return False
        if char == '(':
            count += 1
        else:
            count -= 1
    return count == 0


# считываем данные

txt = input()
# вызываем функцию
print(is_correct_bracket(txt))