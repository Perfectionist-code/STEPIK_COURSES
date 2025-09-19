d = set()

def f(curr, step):
    if step == 15: d.add(curr)
    else:
        f(curr * 2, step + 1)
        f(curr * 2 + 1, step + 1)

f(1,0)
print(len(d))
