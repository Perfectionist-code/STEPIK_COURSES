from ipaddress import ip_network, ip_address

net = ip_network('102.141.0.0/255.255.192.0')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if not ip.count('1') % 7 and ip.endswith('1011'):
        cnt += 1
print(cnt)
