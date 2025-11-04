from ipaddress import ip_network, ip_address

ip_host1 = ip_address('121.171.5.70')
ip_host2 = ip_address('121.171.5.107')

for mask in range(32, 1, -1):
    net1 = ip_network(f'{ip_host1}/{mask}',0)
    net2 = ip_network(f'{ip_host2}/{mask}',0)
    if net1 == net2:
        if net1[0] < ip_host1 < net1[-1] and net2[0] < ip_host2 < net2[-1]:
            print(net1.num_addresses)
            break