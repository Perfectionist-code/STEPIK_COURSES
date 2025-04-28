def string_processing(str1: str):
    for tr_char in infection_trigger:
        if tr_char in str1:
            str1 = str1[str1.find(tr_char) + 1:]
        else:
            return False
    return True


def is_infected(*args):
    res = []
    for i, _str in enumerate(lst):
        _str = ''.join(filter(lambda x: x in infection_trigger,
                              _str))  # удаление всех символов, не содержащихся в infection_trigger
        for char in _str:  # удаление двойных символов 'nn'
            while char + char in _str:
                _str = _str.replace(char + char, char)
        # print(_str)
        if infection_trigger in _str:
            res.append(i + 1)  # добавление номера инфецированного холодильника, если такой нашелся
        elif _str != [] and len(_str) >= len(infection_trigger):
            if string_processing(_str):
                res.append(i + 1)
    return res


lst = [input() for _ in range(int(input()))]
infection_trigger = 'anton'
print(*is_infected(lst))
