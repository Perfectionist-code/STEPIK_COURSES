cnt_watermelon = cnt_melon = 0
for _ in range(int(input())):
    if (choice := input()) == 'арбуз':
        cnt_watermelon += 1
    elif choice == 'дыня':
        cnt_melon += 1
if cnt_watermelon == cnt_melon:
    print('Арбузы и дыни одинаково популярны')
else:
    print(('Дыни популярнее','Арбузы популярнее')[cnt_watermelon > cnt_melon])
