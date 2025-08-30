with open('17_2.txt', 'r') as file:
    max_sum = -1e6
    lst = []
    cnt = 0
    for line in file:
        lst.append(int(line))
    for num in sorted(lst):
        if not (num % 6):
            min_el_6 = num
            break
    a = lst[0]
    for l in lst[1:]:
        b = l
        if all([not (a % min_el_6), not (b % min_el_6)]):
            cnt += 1
            if (d := a + b) > max_sum:
                max_sum = d
        a = b
print(cnt, max_sum)

file = open("17_2.txt")  # открываем файл
nums = []  # создаем список, в который и сохраним все числа из файла
min6 = 100001  # сюда запишем минимальный элемент последовательности, кратный 6
for num in file:  # последовательно проходим по всем числам в файле (каждое дано на новой строке)
    nums.append(int(num))  # преобразуем его из типа str в int и сохраняем в список
    if int(num) % 6 == 0:  # если текущий элемент делится на 6
        min6 = min(min6, int(num))  # перезапишем его в min6 (если он меньше)
pairs = []  # создаем список для сохранения подходящих пар
for i in range(len(nums) - 1):  # перебираем все пары соседних элементов (nums[i] и nums[i + 1])
    if nums[i] % min6 == 0 and nums[i + 1] % min6 == 0:  # если оба числа в паре делятся на min6
        pairs.append(nums[i] + nums[i + 1])  # добавляем сумму текущей пары (она нам подошла)
print(len(pairs), max(pairs))  # выводим количество подходящих пар и максимальную из их сумм
file.close()
