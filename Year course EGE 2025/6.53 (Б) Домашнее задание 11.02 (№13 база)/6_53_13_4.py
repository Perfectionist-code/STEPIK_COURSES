from ipaddress import ip_network

ip_host = '203.155.64.98'
ip_net = '203.155.64.0'

res = None
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if str(net.network_address) == ip_net:
        res = net.prefixlen
print('Ответ:', res)
