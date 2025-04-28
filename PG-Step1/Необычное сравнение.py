str1, str2 = input().lower(), input().lower()
s1 = []
s2 = []
for char in str1:
    if char.isalpha():
        s1.append(char)
for char in str2:
    if char.isalpha():
        s2.append(char)
print(('NO', 'YES')[s1 == s2])
