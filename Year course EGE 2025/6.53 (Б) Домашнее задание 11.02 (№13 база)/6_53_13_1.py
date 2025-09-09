from ipaddress import ip_network

ip_host = '217.8.244.3'
mask = '255.255.252.0'

net = ip_network(f'{ip_host}/{mask}', 0)
print(net)
