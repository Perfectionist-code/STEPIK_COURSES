encrypted_word = input()
d = {int(value): key for key, value in (input().split(': ') for _ in range(int(input())))}
d_encrypted_word = {key: encrypted_word.count(key) for key in set(encrypted_word)}
res = []
for char in encrypted_word:
    res.append(d[d_encrypted_word[char]])
print(''.join(res))