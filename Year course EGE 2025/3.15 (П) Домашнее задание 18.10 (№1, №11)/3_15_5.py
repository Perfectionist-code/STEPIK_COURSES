from itertools import permutations

table = '14 15 17 23 25 28 32 34 35 38 41 43 46 47 51 52 53 64 67 68 71 74 76 82 83 86'
graph = 'АБ БА АГ ГА АЕ ЕА БВ ВБ БД ДБ ВИ ИВ ИД ДИ ИЖ ЖИ ЖГ ГЖ ГД ДГ ЕЖ ЖЕ ГЕ ЕГ ВД ДВ'

graph_set = set(graph.split())
print(*'12345678')
for per in permutations('АБВГДЕЖИ'):
    new_graph = table
    for i in range(8):
        new_graph = new_graph.replace(str(i + 1), per[i])
    if set(new_graph.split()) == graph_set:
        print(*per)
