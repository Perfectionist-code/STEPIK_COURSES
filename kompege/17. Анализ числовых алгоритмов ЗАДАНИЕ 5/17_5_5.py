def num_to_cs(num:int, cs:int) -> str:
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r))
    return ''.join(res[::-1])

def get_r(num:int):
    r = num_to_cs(num, 3)
    r += str(num % 3)
    return int(r, 3)

for n in range(100):
    print(get_r(n))