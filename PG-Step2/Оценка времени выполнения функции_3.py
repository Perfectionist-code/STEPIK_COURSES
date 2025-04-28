import random
import string
import time
import functools

def create_string(length=10_000_000, lower_l=False, upper_l=True, digit=True) -> str:
    """
    Генерирует случайную строку заданной длины из выбранных групп символов.
    """
    random.seed(1)
    my_collection = string.ascii_lowercase * lower_l + string.ascii_uppercase * upper_l + string.digits * digit
    characters = (random.choice(my_collection) for _ in range(length))
    return ''.join(characters)

def measure_time(repeats=10):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(repeats):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                total_time += (end - start)
            average_time = total_time / repeats
            print(f'Среднее время: {average_time:.7f}')
            print(f'Количество элементов: {len(result):_}')
            return result
        return wrapper
    return decorator

letters_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
letters_list = list(letters_str)
morse = ('.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
         '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
         '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...',
         '---..', '----.')

my_dict = dict(zip(letters_list, morse))
my_string = create_string(1_000_000)

@measure_time()
def check_dict(my_string: str, my_dict: dict) -> str:
    translated_string = ''
    for c in my_string:
        if c in my_dict:
            translated_string += my_dict[c] + ' '
    return translated_string

@measure_time()
def check_dict_new_version(my_string: str, my_dict: dict) -> str:
    translated_string = (my_dict[l] for l in my_string if l in my_dict)

    return ' '.join(translated_string)

@measure_time()
def check_new_index(my_string: str, letters: str, morse: tuple) -> str:

    return ' '.join(morse[letters.index(i)] for i in my_string if i in letters)

@measure_time()
def check_list_old_version(my_string: str, letters: list, morse: tuple) -> list:
    return [morse[letters.index(i)] + ' ' for i in my_string if i in letters]

print('Работа со словарём, код команды курса:')
check_dict(my_string, my_dict)
print('-*-' * 20)
print('Работа со словарём, новый код:')
check_dict_new_version(my_string, my_dict)
print('-*-' * 20)
print('Работа с индексом:')
check_new_index(my_string, letters_str, morse)
print('-*-' * 20)
print('Работа с моим старым кодом:')
check_list_old_version(my_string, letters_list, morse)
print('Количество элементов другое, т.к. на выходе список, а не строка')