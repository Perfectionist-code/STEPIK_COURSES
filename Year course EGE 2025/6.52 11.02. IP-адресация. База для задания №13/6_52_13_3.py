from ipaddress import ip_network

ip_host = '215.181.200.27'
ip_net = '215.181.192.0'

res_mask = None
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if str(net).startswith(ip_net):
        res_mask = str(net.netmask)
print(res_mask)
print('Ответ:', res_mask.split('.')[-2])
