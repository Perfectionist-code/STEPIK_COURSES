from ipaddress import ip_network, ip_address

net = ip_network('123.222.111.192/255.255.255.248')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip[-8:].count('1') % 3:
        cnt += 1
print(cnt)
