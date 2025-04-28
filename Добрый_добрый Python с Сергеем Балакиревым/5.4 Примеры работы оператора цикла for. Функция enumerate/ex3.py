# Большой подвиг 3. На вход программе подается строка, в которой записано арифметическое выражение. Например:
#
# "10 + 25 - 12"
#
# или
#
# "10 + 25 - 12 + 20 - 1 + 3"
#
# и т. д. То есть, количество действий может быть произвольным.
#
# Необходимо прочитать эту строку из входного потока и выполнить вычисление, записанного в ней арифметического выражения. Результат вычисления отобразить на экране.
#
# Полагается, что в качестве арифметических операций используется только сложение (+) и вычитание (-), а в качестве операндов только целые неотрицательные числа. Следует учесть, что математические операции могут быть записаны как с пробелами (до и после), так и без них.
#
# P.S. В целях обучения программу следует делать без использования функции eval.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.3
#
# Sample Input:
#
# 10+25 - 12
# Sample Output:
#
# 23

st = input().replace(' ','')
a = len(st)
summ = 0
number_str = ''
for i,d in enumerate(st) :
    if d == '-' and st[i + 1].isdigit() :
        number_str = '-'
    if d == '+' and st[i + 1].isdigit() :
        number_str = ''
    if i < len(st) - 1 :
        if d.isdigit() and st[i + 1].isdigit() :
            number_str += d
        elif d.isdigit() and not st[i + 1].isdigit() :
            number_str += d
            summ += int(number_str)
            number_str = ''
    if i == len(st) - 1 :
        if d.isdigit() :
            number_str += d
            summ += int(number_str)
print(summ)

# Супер решение:
#text = input().replace(' ', '').replace('-', '+-').split('+')
#print(sum(map(int, text)))
# или такое:
#e = map(int, input().replace(' ', '').replace('+', ' +').replace('-', ' -').split())
#print(sum(e))



