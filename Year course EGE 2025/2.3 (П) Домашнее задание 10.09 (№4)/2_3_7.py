for x in range(1,11):
    for y in range(x, 11):
        for z in range(y, 11):
            if 3 * x + 2 *y + z == 17:
                print('-------')
                print(*'xyz')
                print(x,y,z)


