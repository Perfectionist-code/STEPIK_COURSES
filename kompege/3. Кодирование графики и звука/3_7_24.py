V = 500 * 2 ** 23
t_move = 40
t_flash = V / (100 * 2 ** 20)
t_A = 2 * t_flash + t_move
t_B = V / (10 * 2 ** 20)
print('Ответ: ', ('А', 'Б')[t_B < t_A], abs(int(t_B-t_A)), sep='')
