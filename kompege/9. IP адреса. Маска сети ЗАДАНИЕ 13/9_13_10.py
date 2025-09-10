from ipaddress import ip_network, ip_address

ip_host1 = ip_address('10.96.180.231')
ip_host2 = ip_address('10.96.140.118')

for mask in range(33):
    net1 = ip_network(f'{ip_host1}/{mask}', 0)
    net2 = ip_network(f'{ip_host2}/{mask}', 0)
    if all((net1 != net2, net1[0] < ip_host1 < net1[-1], net2[0] < ip_host2 < net2[-1])):
        print('Ответ:', 32 - mask)
        break
