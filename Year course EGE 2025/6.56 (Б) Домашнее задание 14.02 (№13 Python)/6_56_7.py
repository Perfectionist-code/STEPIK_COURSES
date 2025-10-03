from ipaddress import ip_network, ip_address

net = ip_network(f'151.192.0.0/255.224.0.0')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') == 16:
        cnt += 1
print('Ответ:', cnt)
