d = {}
lst = [input().split() for _ in range(int(input()))]
for name, product, num in lst:
    if name not in d:
        d.setdefault(name, {product: int(num)})
    elif product not in d[name]:
        d.get(name).setdefault(product, int(num))
    else:
        d[name][product] += int(num)

for name in sorted(d):
    print(f'{name}:')
    for product in sorted(d[name]):
        print(product, d[name][product])

# data = {}
#
# for _ in range(int(input())):
#     name, product, count = input().split()
#     data.setdefault(name, {})
#     data[name][product] = data[name].get(product, 0) + int(count)
#
# for person, products in sorted(data.items()):
#     print(f'{person}:')
#     for product, count in sorted(products.items()):
#         print(product, count)