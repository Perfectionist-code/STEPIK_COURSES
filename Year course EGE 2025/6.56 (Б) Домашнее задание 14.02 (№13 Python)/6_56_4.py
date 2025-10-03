from ipaddress import ip_network, ip_address

net = ip_network(f'172.16.128.0/255.255.192.0')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') % 2:
        cnt += 1
print('Ответ:', cnt)
