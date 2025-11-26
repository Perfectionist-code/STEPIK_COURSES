from ipaddress import ip_network, ip_address

net = ip_network('172.30.0.0/255.254.0.0')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') % 12:
        cnt += 1
print(cnt)
