from ipaddress import ip_network, ip_address

net = ip_network('105.224.200.224/255.255.255.224')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if not ip.count('1') % 4:
        cnt += 1
print('Ответ:', cnt)
