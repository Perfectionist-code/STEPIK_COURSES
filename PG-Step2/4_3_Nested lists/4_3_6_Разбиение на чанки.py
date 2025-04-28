def chunked(*args):
    _range = len(_str) // _chunk + len(_str) % _chunk
    if len(_str) < _chunk:
        _range = len(_str) - 1
    res = [x for x in (_str[_chunk * y:_chunk * (y + 1)] for y in range(_range))]
    return res


_str = input().split()
_chunk = int(input())
print(chunked(_str, _chunk))


# def chunked(sp, n):
#     return [sp[x:x + n] for x in range(0,len(sp),n)]
#
#
# s = input().split()
# n = int(input())
# print(chunked(s, n))