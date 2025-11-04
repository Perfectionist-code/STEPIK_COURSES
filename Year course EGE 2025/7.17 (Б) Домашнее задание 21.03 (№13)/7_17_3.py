from ipaddress import ip_network, ip_address

ip_net = ip_address('215.181.192.0')
ip_host = ip_address('215.181.200.27')

cnt = 0
for mask in range(33):
    net = ip_network(f'{ip_net}/{mask}', 0)
    if net.network_address == ip_net and ip_host in list(net.hosts()):
        print(net.with_netmask)
