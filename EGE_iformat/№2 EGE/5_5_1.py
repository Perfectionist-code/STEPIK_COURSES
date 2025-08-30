# Выведите все значения переменных

# F=(a→d)∧¬(b→c) истинна.
#
# Пример вывода:
#
# a b c d
# 1 0 1 1
# 0 1 0 0
# 1 1 1 1

print(*'abcd')
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):
                if (a <= d) and (not (b <= c)):
                    print(a, b, c, d)