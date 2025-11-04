from ipaddress import ip_network, ip_address

ip_net = ip_address('176.112.100.128')

for mask in range(32, 1, -1):
    net = ip_network(f'{ip_net}/{mask}', 0)
    if net.network_address == ip_net and net.num_addresses == 16:
        print(net.with_netmask)
