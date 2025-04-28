choices = [input().lower(), input(). lower()]
flag = 'Тимур'
match choices:
    case ['бумага', 'бумага'] | ['камень', 'камень'] | ['ножницы', 'ножницы']:
        flag = 'ничья'
    case 'камень', 'ножницы': pass
    case 'ножницы', 'бумага': pass
    case 'бумага', 'камень': pass
    case _:
        flag = 'Руслан'
print(flag)


# moves = ["камень", "ножницы", "бумага"]
# outcomes = ["ничья", "Руслан", "Тимур"]
#
# timur_move = input()
# ruslan_move = input()
#
# difference = moves.index(timur_move) - moves.index(ruslan_move)
# result = outcomes[difference]
#
# print(result)