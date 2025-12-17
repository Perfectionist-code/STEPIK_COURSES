for p in range(7, 37):
    if not (d := int('2465123', p) + int('251341', p)) % 17:
        print(d // 17)
        break
