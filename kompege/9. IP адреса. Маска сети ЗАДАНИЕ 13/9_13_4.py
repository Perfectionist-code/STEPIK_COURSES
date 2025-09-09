from ipaddress import ip_network, ip_address

ip_host = '122.21.49.91'
ip_net = ip_address('122.21.48.0')

res = None
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net.network_address == ip_net:
        res = mask
        break
print('Ответ:', res)
