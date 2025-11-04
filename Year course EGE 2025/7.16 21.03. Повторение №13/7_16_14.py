from ipaddress import ip_network, ip_address

ip_host = ip_address('175.122.80.13')
ip_net = ip_address('175.122.80.0')
cnt = 0
for mask in range(1, 32):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net.network_address == ip_net and net.num_addresses >= 30:
        if net[0] < ip_host < net[-1]:
            cnt += 1
print(cnt)
