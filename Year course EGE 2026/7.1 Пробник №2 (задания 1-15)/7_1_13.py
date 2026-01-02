from ipaddress import ip_address, ip_network

ip_host = ip_address('77.180.176.14')
mask = '255.255.254.0'

net = ip_network(f'{ip_host}/{mask}', 0)
print(str(max(net.hosts())).replace('.', ''))
