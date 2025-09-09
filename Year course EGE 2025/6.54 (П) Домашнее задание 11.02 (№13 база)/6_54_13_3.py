from ipaddress import ip_network

ip_host1 = '135.13.142.29'
mask1 = '255.255.255.128'
net = ip_network(f'{ip_host1}/{mask1}', 0)
res = []
for address in net:
    res.append(address)
print('Ответ:', str(res[-2]).replace('.', ''))
