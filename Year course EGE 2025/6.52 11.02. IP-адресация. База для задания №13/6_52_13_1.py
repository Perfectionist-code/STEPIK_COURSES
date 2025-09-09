# Для ручного решения

# print(*f'{112:>08b}')
# print(*'_' * 8)
# print(*f'{64:>08b}')
# print(int('11000000',2))

# Решение через модуль ipaddress
from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f'124.128.112.142/{mask}', 0)
    print(net, net.netmask)