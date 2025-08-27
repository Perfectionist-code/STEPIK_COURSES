from itertools import permutations

from PyInstaller.utils.win32.versioninfo import nextDWord

table = '58 34 28 268 17 478 568 13467'
graph = 'ЕВ АД АДЗ ЕЖД ЗБД ЖГ ДБ ВЕЗЖГ'

print(*'12345678')
graph_set = {frozenset(x) for x in graph.split()}
for per in permutations('АБВГДЕЖЗ'):
    new_graph = table
    for x, y in zip('12345678', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {frozenset(x) for x in new_graph.split()}
    if new_graph.__eq__(graph_set):
        print(*per)

