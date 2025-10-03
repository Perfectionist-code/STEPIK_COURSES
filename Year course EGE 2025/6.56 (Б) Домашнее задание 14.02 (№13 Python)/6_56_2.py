from ipaddress import ip_network, ip_address

net = ip_network('115.192.0.0/255.192.0.0')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') % 3:
        cnt += 1
print('Ответ:', cnt)
