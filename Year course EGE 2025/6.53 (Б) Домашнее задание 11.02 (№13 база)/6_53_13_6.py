from ipaddress import ip_network

ip_host = '148.195.140.28'
ip_net = '148.195.140.0'

res = None
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if str(net.network_address) == ip_net:
        res = net.prefixlen
        break
print('Ответ:', res)
