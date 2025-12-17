for p in range(8, 37):
    if not (d := int('11353712', p) + int('135421', p)) % 31:
        print(d // 31)
        break
