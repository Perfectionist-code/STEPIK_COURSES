command = {
    (' ', 0): (' ', 1, 1),
    (' ', 1): (' ', 2, 1),
    ('2', 1): ('3', 1, 1),
    ('3', 1): ('X', 1, 1),
    ('X', 1): ('2', 1, 1),
}


def mt(s: str):
    s = list(f' {s} ')
    q = 0
    i = 0
    while True:
        cmd_t = command[(s[i], q)]
        s[i] = cmd_t[0]
        if cmd_t[1] == 2:
            break
        i += cmd_t[1]
        q = cmd_t[2]
    return ''.join(s).strip()


ss = mt(764 * '2' + 122 * '3' + 114 * 'X')
ss1 = ss
for x in range(10):
    ss = ss1
    if x in (2, 3):
        continue
    ss = ss.replace('X', str(x))
    if sum(int(char) for char in ss) == 3496:
        print(x)
        break
