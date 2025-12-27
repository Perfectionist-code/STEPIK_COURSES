command = {
    (' ', 0): (' ', -1, 1),
    (' ', 1): (' ', 2, 1),
    ('0', 1): ('2', -1, 1),
    ('1', 1): ('0', -1, 1),
    ('2', 1): ('1', -1, 1),
}


def mt(s: str):
    s = list(f' {s} ')
    q = 0
    i = len(s) - 1
    while True:
        cmd_t = command[(s[i, q])]
        s[i] = cmd_t[0]
        if cmd_t[1] == 2:
            break
        i += cmd_t[1]
        q = cmd_t[2]
    return ''.join(s).strip()



