from ipaddress import ip_network

ip_host1 = '121.171.15.70'
ip_host2 = '121.171.3.68'

res_mask = None
for mask in range(33):
    net1 = ip_network(f'{ip_host1}/{mask}', 0)
    net2 = ip_network(f'{ip_host2}/{mask}', 0)
    if net1 == net2:
        res_mask = str(net1.netmask)
print(res_mask)
print('Ответ:', res_mask.split('.')[-2])
