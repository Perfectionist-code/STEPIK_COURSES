res = 0
for i, figure in enumerate(input()):
    if i % 2 and not (figure := int(figure)) % 2:
        res += figure
print(res)
