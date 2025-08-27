from itertools import permutations

table = '12 17 19 21 34 36 38 39 43 45 49 54 57 59 63 68 69 71 75 83 86 89 91 93 94 95 96 98'
graph = 'ДЗ ЗД ЗИ ИЗ ЗЖ ЖЗ ИА АИ АВ ВА ЖА АЖ ЖВ ВЖ ЖЕ ЕЖ ЖБ БЖ ЖГ ГЖ ВЕ ЕВ ЕБ БЕ БГ ГБ ЕГ ГЕ'

graph_set = set(graph.split())
print(*'123456789')
for per in permutations('АБВГДЕЖЗИ'):
    new_graph = table
    for i in range(9):
        new_graph = new_graph.replace(str(i + 1), per[i])
    if set(new_graph.split()) == graph_set:
        print(*per)
