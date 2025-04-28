phone_book = {}
for _ in range(int(input())):
    phone, name = input().split()
    if name not in phone_book:
        phone_book.setdefault(name.capitalize(),[phone])
    else:
        phone_book.setdefault(name.capitalize()).append(phone)
request_lst = [input().capitalize() for _ in range(int(input()))]
for request in request_lst:
    print(*phone_book.get(request, ['абонент не найден']))



# dct = {}
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     dct.setdefault(name, []).append(phone)
# for _ in range(int(input())):
#     print(*dct.get(input().lower(), ['абонент не найден']))