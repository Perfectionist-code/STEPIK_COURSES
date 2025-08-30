with open('17_1.txt', 'r') as file:
    max_sum = -1e10
    cnt = 0
    a = int(file.readline())
    for l in file:
        b = int(l)
        if any([not (a % 3), not(b %3)]):
            cnt += 1
            if (d:=a + b) > max_sum:
                max_sum = d
        a = b
print(cnt, max_sum)

file = open("17_1.txt")  # открываем файл
nums = []  # создаем список, в который сохраним все числа из файла
for num in file:  # последовательно проходим по всем числам в файле (каждое дано на новой строке)
    nums.append(int(num))  # преобразуем его из типа str в int и сохраняем в список
pairs = []  # создаем список для сохранения подходящих пар
for i in range(len(nums) - 1):  # перебираем все пары соседних элементов (nums[i] и nums[i + 1])
    if nums[i] % 3 == 0 or nums[i + 1] % 3 == 0:  # если хотя бы одно число из пары делится на 3
        pairs.append(nums[i] + nums[i + 1])  # добавляем сумму текущей пары (она нам подошла)
print(len(pairs), max(pairs))  # выводим количество подходящих пар и максимальную из их сумм