from ipaddress import ip_network, ip_address

ip_host = ip_address('135.13.142.29')
mask = '255.255.255.128'

print(str(max(ip_network(f'{ip_host}/{mask}', 0).hosts())).replace('.', ''))
