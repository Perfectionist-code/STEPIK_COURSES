# def longest_d_chain(s):
#     # Находим все позиции букв D в строке
#     d_positions = [i for i, char in enumerate(s) if char == 'D']
#     n = len(d_positions)
#
#     if n < 2:
#         return 0  # Нужно как минимум 2 буквы D
#
#     max_length = 0
#
#     # Перебираем все возможные начала цепочки
#     for i in range(n):
#         o_count = 0
#         d_count = 1  # Уже есть одна D в начале
#
#         # Перебираем возможные концы цепочки
#         for j in range(i + 1, n):
#             # Считаем количество O между текущей и предыдущей D
#             start_pos = d_positions[j - 1] + 1
#             end_pos = d_positions[j] - 1
#
#             # Добавляем количество O в текущем сегменте
#             for pos in range(start_pos, end_pos + 1):
#                 if s[pos] == 'O':
#                     o_count += 1
#
#             # Если количество O превышает 2, прерываем цепочку
#             if o_count > 2:
#                 break
#
#             # Вычисляем длину текущей цепочки
#             chain_length = d_positions[j] - d_positions[i] + 1
#
#             # Обновляем максимальную длину
#             if chain_length > max_length:
#                 max_length = chain_length
#
#             d_count += 1
#
#     return max_length
#
#
# # Чтение данных из файла
# def solve_from_file(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         s = file.read().strip()
#
#     return longest_d_chain(s)
#
#
# # Альтернативная версия с оптимизацией (более эффективная)
# def longest_d_chain_optimized(s):
#     d_positions = [i for i, char in enumerate(s) if char == 'D']
#     n = len(d_positions)
#
#     if n < 2:
#         return 0
#
#     max_length = 0
#
#     # Для каждой начальной D
#     for i in range(n):
#         o_count = 0
#
#         # Для каждой конечной D, начиная со следующей после начальной
#         for j in range(i + 1, n):
#             # Считаем O между d_positions[j-1] и d_positions[j]
#             # (только в последнем сегменте)
#             if j > i + 1:
#                 # Для всех сегментов кроме первого
#                 start_pos = d_positions[j - 1] + 1
#                 end_pos = d_positions[j] - 1
#                 segment_o = s[start_pos:end_pos + 1].count('O')
#                 o_count += segment_o
#             else:
#                 # Первый сегмент (между i и i+1)
#                 start_pos = d_positions[i] + 1
#                 end_pos = d_positions[i + 1] - 1
#                 o_count = s[start_pos:end_pos + 1].count('O')
#
#             if o_count <= 2:
#                 chain_length = d_positions[j] - d_positions[i] + 1
#                 if chain_length > max_length:
#                     max_length = chain_length
#             else:
#                 break  # Прерываем, так как дальше будет только хуже
#
#     return max_length
#
#
# # # Тестирование
# # if __name__ == "__main__":
# #     # Примеры для тестирования
# #     test_strings = [
# #         "DFOODACODFOD",  # Пример из объяснения
# #         "DACDFOOD",  # Простой случай
# #         "DOOD",  # Минимальная цепочка
# #         "DAD",  # Тоже подходит
# #         "ACF",  # Нет D
# #         "D",  # Одна D
# #         "DOOODOOOD",  # Несколько сегментов
# #     ]
# #
# #     print("Тестирование функции:")
# #     for i, test_str in enumerate(test_strings):
# #         result = longest_d_chain_optimized(test_str)
# #         print(f"Строка {i + 1}: '{test_str}' -> Длина: {result}")
#
#     # Для работы с файлом
# filename = "04.txt"
# result = solve_from_file(filename)
# print(f"Результат для файла: {result}")
#
#


# # with open('04.txt') as file:
# #     s = file.readline()
# # print((ls := len(s)))
# #
# # m = 0
# # for l in range(ls):
# #     for r in range(l + m, ls):
# #         c = s[l:r + 1]
# #         if c[0] == 'D' and c.count('O') <= 2:
# #             if c[-1] == 'D':
# #                 m = max(m, len(c))
# #                 print(c)
# #         else:
# #             break
# # print(m)


import re


def find_longest_d_chain_regex(s):
    """
    Находит самую длинную цепочку, начинающуюся и заканчивающуюся на D,
    где между любыми двумя соседними D не более 2 букв O
    """
    # Паттерн для поиска валидных сегментов между D
    # [^D]* - любые символы кроме D (0 или более)
    # O? - 0 или 1 буква O
    # [^D]* - любые символы кроме D
    # O? - 0 или 1 буква O
    # [^D]* - любые символы кроме D
    # O? - 0 или 1 буква O
    # [^D]* - любые символы кроме D

    # Паттерн для одного сегмента между D: не более 2 O
    segment_pattern = "[^D]*O?[^D]*O?[^D]*O?[^D]*"

    # Строим полный паттерн: D, затем один или более сегментов, заканчивается D
    pattern = f"D({segment_pattern}D)+"

    # Находим все совпадения
    matches = re.finditer(pattern, s)

    max_length = 0
    best_match = ""

    for match in matches:
        chain = match.group()
        length = len(chain)

        # Дополнительная проверка: между каждой парой соседних D должно быть не более 2 O
        if is_valid_chain(chain):
            if length > max_length:
                max_length = length
                best_match = chain

    return max_length, best_match


def is_valid_chain(chain):
    """Проверяет, что между всеми соседними D в цепочке не более 2 букв O"""
    # Разбиваем цепочку по D, но сохраняем позиции D
    parts = chain.split('D')

    # Первая часть - пустая (цепочка начинается с D), последняя - не пустая (заканчивается D)
    for i in range(1, len(parts) - 1):
        segment = parts[i]
        o_count = segment.count('O')
        if o_count > 2:
            return False

    return True


def find_longest_d_chain_regex_optimized(s):
    """
    Оптимизированная версия с одним регулярным выражением
    """
    # Паттерн, который непосредственно проверяет условие с количеством O
    # Используем lookahead для проверки каждого сегмента
    pattern = r"D(?:(?=([^D]*D))(?=(?:[^D]*O){0,2}[^D]*D))*[^D]*D"

    max_length = 0
    best_match = ""

    # Ищем все возможные цепочки
    for i in range(len(s)):
        if s[i] == 'D':
            # Для каждой начальной D ищем самую длинную валидную цепочку
            current_chain = "D"
            o_count = 0
            last_d_pos = i

            for j in range(i + 1, len(s)):
                if s[j] == 'D':
                    # Проверяем сегмент между последней D и текущей
                    segment = s[last_d_pos + 1:j]
                    segment_o_count = segment.count('O')

                    if o_count + segment_o_count <= 2:
                        # Сегмент валиден
                        current_chain += segment + "D"
                        o_count = 0  # Сбрасываем для следующего сегмента
                        last_d_pos = j

                        # Обновляем максимум
                        if len(current_chain) > max_length:
                            max_length = len(current_chain)
                            best_match = current_chain
                    else:
                        # Сегмент невалиден, начинаем новую цепочку с этой D
                        break
                else:
                    # Продолжаем накапливать цепочку
                    current_chain += s[j]

            # Проверяем цепочку, заканчивающуюся на последний символ (если это D)
            if len(current_chain) > max_length and current_chain[-1] == 'D':
                max_length = len(current_chain)
                best_match = current_chain

    return max_length, best_match


def solve_with_regex(filename):
    """Основная функция для решения задачи из файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        s = file.read().strip()

    # Используем оптимизированную версию
    max_length, chain = find_longest_d_chain_regex_optimized(s)
    return max_length, chain


# Альтернативное решение с использованием расширенного регулярного выражения
def find_with_complex_regex(s):
    """
    Попытка использовать одно сложное регулярное выражение
    """
    # Этот паттерн пытается охватить все валидные цепочки
    pattern = r"D(?:[^D]*(?:O[^D]*)?(?:O[^D]*)?(?:O[^D]*)?D)*"

    max_length = 0
    for match in re.finditer(pattern, s):
        candidate = match.group()
        # Проверяем, что цепочка заканчивается на D и удовлетворяет условиям
        if candidate.endswith('D') and is_valid_chain(candidate):
            if len(candidate) > max_length:
                max_length = len(candidate)

    return max_length


# Тестирование
# if __name__ == "__main__":
#     # Тестовые примеры
#     test_cases = [
#         "DFOODACODFOD",  # Должна найти цепочку длиной 12
#         "DACDFOOD",  # D A C D F O O D -> длина 8
#         "DOOD",  # D O O D -> длина 4
#         "DAD",  # D A D -> длина 3
#         "DOOADOOD",  # D O O A D O O D -> длина 8
#         "ACF",  # Нет D -> 0
#         "D",  # Одна D -> 0
#     ]
#
#     print("Тестирование регулярных выражений:")
#     print("-" * 50)
#
#     for i, test_str in enumerate(test_cases, 1):
#         length1, chain1 = find_longest_d_chain_regex(test_str)
#         length2, chain2 = find_longest_d_chain_regex_optimized(test_str)
#         length3 = find_with_complex_regex(test_str)
#
#         print(f"Тест {i}: '{test_str}'")
#         print(f"  Метод 1: длина = {length1}, цепочка = '{chain1}'")
#         print(f"  Метод 2: длина = {length2}, цепочка = '{chain2}'")
#         print(f"  Метод 3: длина = {length3}")
#         print()

# Для использования с файлом:
result = solve_with_regex("04.txt")
print(f"Результат: {result}")