from ipaddress import ip_network

ip_host1 = '113.188.14.51'
ip_host2 = '113.188.6.86'
for mask in range(33):
    net1 = ip_network(f'{ip_host1}/{mask}', 0)
    net2 = ip_network(f'{ip_host2}/{mask}', 0)
    if net1 == net2:
        net = net1
cnt = 0
for ip in net:
    if f'{ip:b}'.count('1') == 17:
        cnt += 1
print('Ответ:', cnt)
