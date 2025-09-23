from ipaddress import ip_address, ip_network

net = ip_network('192.168.32.160/255.255.255.240')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if not ip.count('1') % 2:
        cnt += 1
print('Ответ:', cnt)
