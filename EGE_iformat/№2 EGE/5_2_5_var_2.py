cnt = 0
for _ in range(int(input())):
    if (choice := input()) == 'арбуз':
        cnt += 1
    elif choice == 'дыня':
        cnt -= 1
if cnt:
    print(('Дыни популярнее', 'Арбузы популярнее')[cnt > 0])
else:
    print('Арбузы и дыни одинаково популярны')