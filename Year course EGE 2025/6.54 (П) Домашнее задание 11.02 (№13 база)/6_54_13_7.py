from ipaddress import ip_network


def count_ip_addresses(network) -> int:
    cnt = 0
    for ip in network:
        if f'{ip:b}'.count('1') == 18:
            cnt += 1
    return cnt


ip_host = '196.138.142.89'
for mask in range(32,1,-1):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if count_ip_addresses(net) == 78:
        print('Ответ:', mask)
        break
