from itertools import permutations

table = '12347 216 3158 4157 5348 6278 7146 8356'
graph = 'ACBD BADE CAHF DFABG EBGH FCD GHDE HCGE'

print(*'12345678')

graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('ABCDEFGH'):
    new_graph = table
    for x, y in zip('12345678', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)
# 1-7 = 10
# 4-5 = 4
# 10 + 4 = 14
