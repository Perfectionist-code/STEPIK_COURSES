from ipaddress import ip_network

net = ip_network('112.160.0.0/255.240.0.0')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if not ip.count('1') % 5:
        cnt += 1
print('Ответ:', cnt)
