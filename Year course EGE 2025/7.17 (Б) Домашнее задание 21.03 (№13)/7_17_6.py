from ipaddress import ip_network, ip_address

net = ip_network('176.112.100.128/255.255.255.224')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') % 2:
        cnt += 1
print(cnt)
