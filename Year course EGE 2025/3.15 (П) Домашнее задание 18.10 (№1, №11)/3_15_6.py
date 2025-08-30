from itertools import permutations

table = '12 15 16 21 24 25 26 28 34 35 42 43 51 52 53 61 62 67 76 78 82 87'
graph = 'АЕ ЕА АГ ГА ЕЖ ЖЕ ГЖ ЖГ ГБ БГ БД ДБ ЖБ БЖ ЖД ДЖ ЖИ ИЖ ИВ ВИ ДВ ВД'

graph_set = set(graph.split())
print(*'12345678')
for per in permutations('АБВГДЕЖИ'):
    new_graph = table
    for i in range(8):
        new_graph = new_graph.replace(str(i + 1), per[i])
    if set(new_graph.split()) == graph_set:
        print(*per)
