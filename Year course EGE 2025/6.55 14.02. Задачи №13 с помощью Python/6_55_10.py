from ipaddress import ip_network, ip_address


def condition(net_an) -> bool:
    for ip in net:
        ip = f'{ip:b}'
        if ip[:16].count('0') > ip[16:].count('0'):
            return False
    return True


ip_host = ip_address('243.46.4.198')

for A in range(0, 256):
    mask = f'255.255.{A}.0'
    try:
        net = ip_network(f'{ip_host}/{mask}', 0)
        if net[0] < ip_host < net[-1] and condition(net):
            print(A)
            break
    except ValueError:
        continue
