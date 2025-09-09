from ipaddress import ip_network

ip_host = '111.81.208.27'
ip_net = '111.81.192.0'

res = None
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if str(net.network_address) == ip_net:
        res = str(net.netmask).split('.')[-2]
        break
print('Ответ:', res)
