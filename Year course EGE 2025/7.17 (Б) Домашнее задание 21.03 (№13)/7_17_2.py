from ipaddress import ip_network, ip_address

ip_net = ip_address('158.116.0.0')
ip_host = ip_address('158.116.11.146')

cnt = 0
for mask in range(33):
    net = ip_network(f'{ip_net}/{mask}', 0)
    if net.network_address == ip_net and ip_host in list(net.hosts()):
        cnt += 1
print(cnt)
