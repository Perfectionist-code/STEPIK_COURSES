from itertools import permutations

from PyInstaller.utils.win32.versioninfo import nextDWord

table = '4578 367 26 15 148 238 128 1567'
graph = 'БИ АВИЖ БЖГ ВДЕ ГЕ ЖГД ЕВБИ АЖБ'
print(*'12345678')
graph_set = {frozenset(x) for x in graph.split()}
for per in permutations('АБВГДЕЖИ'):
    new_graph = table
    for x, y in zip('12345678', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {frozenset(x) for x in new_graph.split()}
    if new_graph.__eq__(graph_set):
        print(*per)
