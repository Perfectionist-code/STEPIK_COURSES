from ipaddress import ip_network, ip_address


def count_ip(network) -> int:
    cnt = 0
    for ip in network:
        ip = f'{ip:b}'
        if not ip.count('1') % 3 and ip.endswith('11'):
            cnt += 1
    return cnt


ip_net = ip_address('94.149.96.0')
mask = ip_address('255.255.224.0')
net = ip_network(f'{ip_net}/{mask}')
print('Ответ:', count_ip(net))
