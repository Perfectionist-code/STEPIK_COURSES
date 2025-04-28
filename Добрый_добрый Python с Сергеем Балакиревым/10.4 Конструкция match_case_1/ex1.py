# Подвиг 5. Пользователь может ввести с клавиатуры следующие команды в виде строки:
#
# top или Top или TOP
# bottom или Bottom или BOTTOM
# right или Right или RIGHT
# left или Left или LEFT
#
# cmd = input()
# С помощью оператора match/case необходимо определить тип команды cmd и при совпадении вывести на экран сообщение в формате:
#
# Команда <название команды малыми буквами>
#
# Например, при вводе Top, должны на выходе получить:
#
# Команда top
#
# И так для всех четырех команд. Если тип команды не определен, то вывести строку:
#
# Неверная команда
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.4.5
#
# Sample Input:
#
# BOTTOM
# Sample Output:
#
# Команда bottom

cmd = input()
match cmd:
    case command if command in ('top', 'Top', 'TOP'):
        print('Команда', command.lower())
    case command if command in ('bottom', 'bottom'.title(), 'bottom'.upper()):
        print('Команда', command.lower())
    case command if command in ('right'.lower(), 'right'.title(), 'right'.upper()):
        print('Команда', command.lower())
    case command if command in ('left'.lower(), 'left'.title(), 'left'.upper()):
        print('Команда', command.lower())
    case _:
        print('Неверная команда')


# match (cmd := input()):
#     case 'top' | 'Top' | 'TOP' as res: pass
#     case 'bottom' | 'Bottom' | 'BOTTOM' as res: pass
#     case 'right' | 'Right' | 'RIGHT' as res: pass
#     case 'left' | 'Left' | 'LEFT' as res: pass
#     case _: res = None
# print('Неверная команда' if res is None else f'Команда {cmd.lower()}')