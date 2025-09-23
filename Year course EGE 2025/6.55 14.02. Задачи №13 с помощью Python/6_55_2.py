from ipaddress import ip_address, ip_network

net = ip_network('112.208.0.0/255.255.128.0')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if not ip.count('1') % 11:
        cnt += 1
print('Ответ:', cnt)
