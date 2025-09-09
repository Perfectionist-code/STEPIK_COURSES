from ipaddress import ip_network

ip_host1 = '61.58.73.42'
ip_host2 = '61.58.75.136'

res = None
for mask in range(33):
    net1 = ip_network(f'{ip_host1}/{mask}', 0)
    net2 = ip_network(f'{ip_host2}/{mask}', 0)
    if net1 == net2:
        res = str(net1.netmask).split('.')[-2]
print('Ответ:', res)
