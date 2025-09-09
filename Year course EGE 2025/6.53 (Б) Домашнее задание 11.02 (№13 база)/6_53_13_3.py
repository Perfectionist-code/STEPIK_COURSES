from ipaddress import ip_network

ip_host = '15.51.208.15'
ip_net = '15.51.192.0'

for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if str(net.network_address) == ip_net:
        net_mask = net.netmask
        print(net_mask)
print('Ответ:', str(net_mask).split('.')[-2])
