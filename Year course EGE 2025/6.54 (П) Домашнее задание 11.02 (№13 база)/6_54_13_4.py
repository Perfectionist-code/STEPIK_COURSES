from ipaddress import ip_network

ip_host1 = '126.115.78.15'
ip_host2 = '126.115.84.26'
res_net = None
for mask in range(33):
    net1 = ip_network(f'{ip_host1}/{mask}', 0)
    net2 = ip_network(f'{ip_host2}/{mask}', 0)
    if net1 == net2:
        net = net1
cnt = 0
for ip in net:
    if f'{ip:b}'.count('1') == 22:
        cnt += 1
print('Ответ:', cnt)
