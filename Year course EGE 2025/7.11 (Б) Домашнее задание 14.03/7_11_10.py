from ipaddress import ip_network, ip_address

ip_host = ip_address('111.91.200.28')

for mask in range(32, 0, -1):
    net = ip_network(f'111.91.192.0/{mask}', 0)
    if net[0] < ip_host < net[-1]:
        print('Ответ:', 32 - mask)
        break
