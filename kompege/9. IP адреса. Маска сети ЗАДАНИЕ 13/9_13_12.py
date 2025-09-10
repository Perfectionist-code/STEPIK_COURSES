from ipaddress import ip_network, ip_address

ip_net = ip_address('10.48.96.0')
mask = ip_address('255.255.240.0')

net = ip_network(f'{ip_net}/{mask}')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') > 16:
        cnt += 1
print(cnt)
