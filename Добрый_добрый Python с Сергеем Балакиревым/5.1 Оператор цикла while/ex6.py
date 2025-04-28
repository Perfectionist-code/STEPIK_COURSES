# Подвиг 7. На вход программе подается натуральное число (то есть, целое положительное) от трехзначного и более. Необходимо прочитать это число и найти произведение всех его цифр. Результат (произведение) вывести на экран. Программу реализовать при помощи цикла while.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.1.7
#
# Sample Input:
#
# 821
# Sample Output:
#
# 16

#a = int(input())
i = 0
a = input()
lenght = len(a)
b = list(a)
res = 1
while i <= lenght-1:
    if b[i] != 0:
        res *= int(b[i])
        i += 1
    else:
        res = 0
print(res)