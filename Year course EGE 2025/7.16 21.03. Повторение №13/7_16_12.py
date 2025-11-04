from ipaddress import ip_network, ip_address

net = ip_network('192.168.31.80/255.255.255.240')

res = []
for ip in net:
    ip = f'{ip:b}'
    res.append(ip.count('1'))

print(max(res))
