from ipaddress import ip_network, ip_address

net = ip_network(f'192.168.72.128/255.255.255.128')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if not ip.count('1') % 10:
        cnt += 1
print('Ответ:', cnt)
