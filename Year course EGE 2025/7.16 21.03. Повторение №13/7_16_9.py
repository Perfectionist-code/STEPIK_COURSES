from ipaddress import ip_network, ip_address

net = ip_network('122.159.136.144/255.255.255.248')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') % 4:
        cnt += 1
print(cnt)
