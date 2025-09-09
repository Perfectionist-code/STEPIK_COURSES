from ipaddress import ip_network, ip_address

ip_host = '118.193.30.139'
ip_net = ip_address('118.193.24.0')
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net.network_address == ip_net:
        res = str(net.netmask).split('.')[-2]
        break
print('Ответ:', res)

