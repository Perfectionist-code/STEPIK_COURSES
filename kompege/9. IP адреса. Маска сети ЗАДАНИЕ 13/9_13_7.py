from ipaddress import ip_network, ip_address

ip_host = ip_address('191.173.145.240')
ip_net = ip_address('191.173.144.0')

cnt = 0
for mask in range(32,-1,-1):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net.network_address == ip_net and net[0] < ip_host < net[-1]:
        print('Ответ:', net.num_addresses)
        break
