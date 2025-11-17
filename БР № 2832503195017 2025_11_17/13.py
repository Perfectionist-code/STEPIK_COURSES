from ipaddress import ip_network, ip_address

ip_host = ip_address('118.193.30.139')
ip_net = ip_address('118.193.24.0')

for mask in range(0, 33):
    net = ip_network(f'{ip_host}/{mask}',0)
    if net.network_address == ip_net and ip_host in net.hosts():
        print(net.with_netmask)
