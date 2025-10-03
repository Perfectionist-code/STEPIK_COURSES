from ipaddress import ip_network, ip_address

net = ip_network(f'171.128.0.0/255.128.0.0')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip[:16].count('1') < ip[16:].count('1'):
        cnt += 1
print('Ответ:', cnt)
