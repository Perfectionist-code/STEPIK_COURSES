from ipaddress import ip_network, ip_address


def condition_1(network) -> bool:
    print('--------' * 10)
    print(network.with_netmask)
    for ip in network:
        ip = f'{ip:b}'
        print(ip, end=' - ')
        if ip[:16].count('0') >= ip[16:].count('0'):
            print(True)
        else:
            print(False)
            return False
    else:
        return True


ip_host = ip_address('152.65.245.132')

for A in range(0, 256):
    mask = ip_address(f'255.255.{A}.0')
    try:
        net = ip_network(f'{ip_host}/{mask}', 0)
        if net[0] < ip_host < net[-1] and condition_1(net):
            print('Ответ:', A)
            break
    except ValueError:
        # print('ValueError with A =', A)
        continue