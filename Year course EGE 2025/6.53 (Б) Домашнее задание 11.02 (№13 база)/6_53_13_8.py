from ipaddress import ip_network

net = ip_network('0.0.0.0/255.255.255.128')
print('Ответ:', net.num_addresses - 2)
