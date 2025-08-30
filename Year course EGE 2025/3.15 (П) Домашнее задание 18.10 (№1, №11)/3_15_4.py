from itertools import permutations

table = '13 15 17 24 25 26 31 38 42 46 47 48 51 52 56 62 64 65 71 74 78 83 84 87'
graph_origin = 'АБ БА АГ ГА АЕ ЕА БГ ГБ ГЕ ЕГ БВ ВБ ЕЖ ЖЕ ВД ДВ ВИ ИВ ДЖ ЖД ЖИ ИЖ'
possibly_missed = ('ЕВ ВЕ', 'ГВ ВГ', 'ГД ДГ', 'ГЖ ЖГ', 'ДИ ИД', 'БД ДБ')

for road in possibly_missed:
    graph = f'{graph_origin} {road}'
    print('-----' * 5, road.split()[0])
    print(*'12345678')
    graph_set = set(graph.split())
    for per in permutations('АБВГДЕЖИ'):
        new_graph = table
        for i in range(8):
            new_graph = new_graph.replace(str(i + 1), per[i])
        if set(new_graph.split()) == graph_set:
            print(*per)

