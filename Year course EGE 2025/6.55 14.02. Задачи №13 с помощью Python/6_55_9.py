from ipaddress import ip_network, ip_address


def condition(net_an) -> bool:
    for ip in net:
        ip = f'{ip:b}'
        if ip[:16].count('1') < ip[16:].count('1'):
            return False
    return True


mask = '255.255.255.192'
cnt = 0
for A in range(255, 0, -1):
    ip_host = ip_address(f'250.113.{A}.197')
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net[0] < ip_host < net[-1] and condition(net):
        print('Ответ:', A)
        break