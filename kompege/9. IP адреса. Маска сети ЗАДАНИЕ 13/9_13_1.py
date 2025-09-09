ip_host = '10.8.248.131'
mask ='255.255.224.0'

# Ручной вариант решения
# ip_host = '.'.join((f'{x:>08b}' for x in map(int, ip_host.split('.'))))
# mask = '.'.join((f'{x:>08b}' for x in map(int, mask.split('.'))))
# print(*ip_host)
# print(*'_' * 32)
# print(*mask)
# print(int('11100000', 2))

# Решение с помощью модуля ipaddress
from ipaddress import ip_network
print(ip_network(f'{ip_host}/{mask}', 0))
