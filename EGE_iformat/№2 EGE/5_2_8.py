for i in range(int(input()), 1 + int(input())):
    if all((not i % 12, not i % 14)):
        print(i)
        break
