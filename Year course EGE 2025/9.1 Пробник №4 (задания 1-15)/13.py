from ipaddress import ip_address, ip_network

net = ip_network('204.16.168.0/255.255.248.0')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') % 5:
        cnt += 1
print(cnt)
