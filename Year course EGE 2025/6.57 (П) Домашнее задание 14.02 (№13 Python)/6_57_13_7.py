from ipaddress import ip_network, ip_address


def counter_ip(net):
    cnt = 0
    for ip in net:
        if f'{ip:b}'.count('1') == 15:
            cnt += 1
    return cnt


ip1 = ip_address('157.220.185.237')
ip2 = ip_address('157.220.184.230')

for mask in range(31, -1, -1):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)
    if all((net1 == net2, net1[0] < ip1 < net1[-1], net1[0] < ip2 < net1[-1], bool(res := counter_ip(net1)))):
        print('Ответ:', res)
        break
