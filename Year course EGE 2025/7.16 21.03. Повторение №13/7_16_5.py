from ipaddress import ip_network, ip_address

ip_host1 = ip_address('161.137.200.35')
ip_host2 = ip_address('161.137.150.118')

for mask in range(1, 32):
    net1 = ip_network(f'{ip_host1}/{mask}',0)
    net2 = ip_network(f'{ip_host2}/{mask}',0)
    if net1 == net2:
        if net1[0] < ip_host1 < net1[-1] and net1[0] < ip_host2 < net1[-1]:
            print(net1.network_address)