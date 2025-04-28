# from string import ascii_lowercase
# ascii_lowercase_extended = ascii_lowercase * 2
# shift, encrypted_message = int(input()), input()
# decrypted_message = []
# for char in encrypted_message:
#     decrypted_message.append(ascii_lowercase_extended[ascii_lowercase_extended.rindex(char) - shift])
# print(*decrypted_message, sep = '')

n = int(input())
s = input()
res = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(s)):
    res += alphabet[alphabet.find(s[i])-n]
    print(alphabet.find(s[i]), alphabet.find(s[i])-n)
print(res)
