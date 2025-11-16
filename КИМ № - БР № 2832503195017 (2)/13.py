from ipaddress import ip_network, ip_address

net = ip_network('192.168.32.160/255.255.255.240')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('0') > 21:
        cnt += 1
print(cnt)
