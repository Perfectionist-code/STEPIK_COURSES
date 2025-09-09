from ipaddress import ip_network, ip_address

ip_host = '173.103.25.118'
ip_net = ip_address('173.103.24.0')

res = None
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net.network_address == ip_net:
        res = mask
        break
print('Ответ:', 32 - res)
