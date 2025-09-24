from ipaddress import ip_network

net = ip_network('123.222.0.192/255.255.255.224')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') == 16:
        cnt += 1
print('Ответ:', cnt)
