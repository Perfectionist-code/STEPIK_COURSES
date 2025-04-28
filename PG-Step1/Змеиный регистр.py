# объявление функции
from string import ascii_uppercase


def convert_to_python_case(text):
    for char in text:
        if char in ascii_uppercase:
            text = text.replace(char, '_' + char.lower())
    return text.lstrip('_')


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
