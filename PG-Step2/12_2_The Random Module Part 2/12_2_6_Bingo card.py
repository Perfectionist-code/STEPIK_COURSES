from random import sample

random_lst = sample(range(1, 76), 25)
bingo_card_matrix = [random_lst[5 * i:5 * i + 5] for i in range(5)]
bingo_card_matrix[2][2] = 0
for row in bingo_card_matrix:
    print(*row, sep = '\t')
