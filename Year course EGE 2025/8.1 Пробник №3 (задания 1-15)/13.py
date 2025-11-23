from ipaddress import ip_network, ip_address

ip_host = ip_address('137.219.220.63')

cnt = 0
for mask in range(32, 1, -1):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if ip_host != net[-1]:
        print(mask)
        break
