from ipaddress import ip_network

ip_host = '10.8.248.131'
mask = '255.255.224.0'
net = ip_network(f'{ip_host}/{mask}', 0)
print(net.network_address)
