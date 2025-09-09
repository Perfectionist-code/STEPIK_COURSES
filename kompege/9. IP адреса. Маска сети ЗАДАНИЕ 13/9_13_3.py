from ipaddress import ip_network, ip_address

ip_host = '154.201.208.17'
ip_net = ip_address('154.201.192.0')

res = None
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net.network_address == ip_net:
        res = net.netmask
print('Ответ:', str(res).split('.')[-2])
