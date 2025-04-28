from string import ascii_lowercase


# объявление функции
def is_pangram(text):
    set1 = set(ascii_lowercase)
    set2 = set(text.replace(' ', '').lower())
    return (set1 - set2) == set()


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
