from ipaddress import ip_network, ip_address

net = ip_network(f'123.222.99.192/255.255.255.248')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('0') < 16:
        cnt += 1
print('Ответ:', cnt)
