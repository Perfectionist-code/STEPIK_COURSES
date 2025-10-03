from ipaddress import ip_network, ip_address

net = ip_network(f'214.96.0.0/255.240.0.0')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if not ip.count('0') % 3:
        cnt += 1
print('Ответ:', cnt)
