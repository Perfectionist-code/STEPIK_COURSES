from ipaddress import ip_network

ip_host1 = '123.215.104.78'
mask1 = '255.255.252.0'
net = ip_network(f'{ip_host1}/{mask1}', 0)
res = []
for address in net:
    res.append(address)
print('Ответ:', str(res[-2]).replace('.', ''))
