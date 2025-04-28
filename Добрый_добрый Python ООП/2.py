def kaprekar_step(l):
    l = ''.join(map(str, l))
    return abs(int(''.join(sorted(l))) - int(''.join(sorted(l, reverse=True))))

def kaprekar_loop(n):
    while n != 6174:
        print(n)
        n = kaprekar_step([int(x) for x in str(n)])
    else:
        print(n)




kaprekar_loop(8654)