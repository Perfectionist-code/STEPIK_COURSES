import time
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def remove(func):
    def wrapper(stroka):
        ls = func(stroka).replace('-', ' ').split()
        # print(ls)
        return '-'.join(ls)
    return wrapper


@remove
def convert(strings):
    lst = [t.get(i, i) if i not in ':;.,_' else '-' for i in strings.lower()]
    # print(lst)
    # print(''.join(lst))
    return ''.join(lst)


s = input()
st = time.time_ns()
print(convert(s))
et = time.time_ns()
dt = et - st
print(dt)