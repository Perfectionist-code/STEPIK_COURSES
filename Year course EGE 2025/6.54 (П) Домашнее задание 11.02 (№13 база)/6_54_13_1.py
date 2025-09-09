from ipaddress import ip_network

ip_host1 = '193.45.192.104'
ip_host2 = '193.45.206.210'

res = []
for mask in range(33):
    net1 = ip_network(f'{ip_host1}/{mask}', 0)
    net2 = ip_network(f'{ip_host2}/{mask}', 0)
    if net1 != net2 and net1.prefixlen == net2.prefixlen:
        res.append(str(net1.netmask).split('.')[-2])
print('Ответ:', min(res))
