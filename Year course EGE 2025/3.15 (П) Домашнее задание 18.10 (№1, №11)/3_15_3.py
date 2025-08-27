from itertools import permutations

table = '12 13 15 21 23 24 27 31 32 35 42 47 51 53 56 57 65 67 72 74 75 76'
graph = 'АБ БА АВ ВА АГ ГА БВ ВБ ВГ ГВ БЖ ЖБ БЕ ЕБ ЖЕ ЕЖ ГД ДГ ГЕ ЕГ ДЕ ЕД'

print(*'1234567')
graph_set = set(graph.split())
for per in permutations('АБВГДЕЖ'):
    new_graph = table
    for i in range(7):
        new_graph = new_graph.replace(str(i+1), per[i])
    if set(new_graph.split()) == graph_set:
        print(*per)