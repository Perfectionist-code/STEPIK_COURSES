from ipaddress import ip_network, ip_address

ip_host = ip_address('158.116.11.146')
cnt = 0
for mask in range(33):
    net = ip_network(f'158.116.11.146/{mask}', 0)
    if net[0] < ip_host < net[-1] and str(net.network_address) == '158.116.0.0':
        cnt += 1
        print(net)
print('Ответ:', cnt)
