def solve():
    # Открываем файл для чтения
    with open("26var01.txt", "r") as file:
        # Читаем и разбиваем данные
        data = file.read().strip().split()
        # print(data)

    # Чтение размеров поля и количества занятых клеток
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])

    # T[c] = номер первой занятой (сверху) строки в столбце c
    # Если столбец c пуст - считаем, что первая занятая строка = M+1
    T = [M + 1] * (K + 1)  # для удобства 1-based индексация столбцов


    idx = 3
    for _ in range(N):
        r = int(data[idx])
        c = int(data[idx + 1])
        idx += 2
        if r < T[c]:
            T[c] = r


    best_r = 0  # искомая строка (максимально возможная)
    best_c = 1  # столбец, при котором достигается best_r, берём минимальный

    for c in range(1, K):
        # корабль из двух клеток займёт столбцы c и c+1 в строке r_possible
        r_possible = min(T[c], T[c + 1]) - 1
        # выбираем максимально возможный r, а при равенстве - столбец поменьше
        if r_possible > best_r:
            best_r = r_possible
            best_c = c

    # Выводим результат в консоль
    print(best_r, best_c)


# Вызываем функцию
solve()