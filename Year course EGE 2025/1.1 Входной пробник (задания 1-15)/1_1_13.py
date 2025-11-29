from ipaddress import ip_network, ip_address

net = ip_network('116.29.170.89/255.255.255.224', 0)

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip[:16].count('1') >= ip[16:].count('1'):
        cnt += 1
print(cnt)
