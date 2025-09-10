from ipaddress import ip_network, ip_address

ip_host = ip_address('158.116.11.146')
ip_net = ip_address('158.116.0.0')

cnt = 0
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net.network_address == ip_net and net[0] < ip_host < net[-1]:
        cnt += 1
print('Ответ:', cnt)
