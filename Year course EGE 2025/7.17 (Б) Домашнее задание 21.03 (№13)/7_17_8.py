from ipaddress import ip_network, ip_address

ip_host = ip_address('98.112.180.225')
mask = '255.255.240.0'

print(str(max(ip_network(f'{ip_host}/{mask}',0).hosts())).replace('.',''))
