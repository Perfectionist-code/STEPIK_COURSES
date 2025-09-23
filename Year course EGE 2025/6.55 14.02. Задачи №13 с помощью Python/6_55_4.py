from ipaddress import ip_network

net = ip_network('10.48.96.0/255.255.240.0')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') > 16:
        cnt += 1
print('Ответ:', cnt)
