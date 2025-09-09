from ipaddress import ip_network

ip_host = '121.74.179.135'
ip_net = '121.74.179.128'

num = []
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if str(net.network_address) == ip_net:
        num.append(net.num_addresses)
print('Ответ:', max(num))
