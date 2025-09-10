from ipaddress import ip_network, ip_address

ip_host = ip_address('192.168.240.0')
mask = ip_address('255.255.255.0')

net = ip_network(f'{ip_host}/{mask}')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('0') == 16:
        cnt += 1
print(cnt)
