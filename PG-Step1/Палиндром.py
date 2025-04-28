# объявление функции
def is_palindrome(text ):
    res = text.lower()
    for i in ',.!?- ':
        res = res.replace(i, '')
    return res == res[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))