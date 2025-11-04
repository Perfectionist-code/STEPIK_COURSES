from ipaddress import ip_network, ip_address

net = ip_network('235.86.56.0/255.255.248.0')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.endswith('11'):
        cnt += 1
print(cnt)
