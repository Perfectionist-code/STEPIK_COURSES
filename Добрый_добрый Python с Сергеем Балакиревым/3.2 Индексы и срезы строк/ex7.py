# Подвиг 10. На вход программе подается строка,
# состоящая из двух слов, записанных через пробел.
# Длина первого слова меньше второго. Необходимо прочитать строку,
# выделить из нее слова и обрезать второе слово до длины первого.
# Полученное (обрезанное) слово выведите в консоль (на экран).
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/3/3.2.10
#
# Sample Input:
#
# Hello Balakirev
# Sample Output:
#
# Balak
str1 = input()
word1, word2 = map(str.strip, str1.split())
word2 = word2[:len(word1)]
print(word2)