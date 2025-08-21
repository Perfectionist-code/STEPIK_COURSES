from itertools import permutations

table = '14 16 17 18 23 24 27 28 32 37 41 42 45 48 54 56 58 61 65 68 71 72 73 78 81 82 84 85 86 87'
graph = 'ВЕ ЕВ ВА АВ ВД ДВ ВЖ ЖВ ЕБ БЕ ЕД ДЕ ЕЗ ЗЕ БА АБ БД ДБ АД ДА ЗГ ГЗ ЗД ДЗ ГЖ ЖГ ЗЖ ЖЗ ЖД ДЖ'

print('1 2 3 4 5 6 7 8')
graph_set = set(graph.split())
for per in permutations('АБВГДЕЖЗ'):
    new_graph = table
    for i in range(8):
        new_graph = new_graph.replace(str(i + 1), per[i])
    if graph_set == set(new_graph.split()):
        print(*per)