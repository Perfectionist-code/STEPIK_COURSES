from ipaddress import ip_network, ip_address


def cond(n) -> bool:
    for ip in n:
        ip = f'{ip:b}'
        if ip[:16].count('0') > ip[16:].count('0'):
            return False
    return True


mask = '255.255.254.0'
for A in range(255, -1, -1):
    try:
        ip_host = ip_address(f'217.109.{A}.94')

        net = ip_network(f'{ip_host}/{mask}', 0)
        if net[0] < ip_host < net[-1] and cond(net):
            print('Ответ:', A)
            break
    except:
        continue
