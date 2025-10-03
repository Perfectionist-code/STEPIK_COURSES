from ipaddress import ip_network, ip_address

net = ip_network(f'195.102.65.64/255.255.255.192')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip[24:].count('0') == 4:
        cnt += 1
print('Ответ:', cnt)
