from ipaddress import ip_network, ip_address

ip_host = ip_address('0.0.0.0')
mask = ip_address('255.255.240.0')
net = ip_network(f'{ip_host}/{mask}', 0)
print('Ответ:', net.num_addresses - 2)
