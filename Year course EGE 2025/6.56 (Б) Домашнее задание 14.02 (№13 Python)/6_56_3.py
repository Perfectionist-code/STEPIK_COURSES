from ipaddress import ip_network, ip_address

ip_host = ip_address('228.172.236.0')
net = ip_network(f'{ip_host}/255.255.240.0', 0)
if net[0] < ip_host < net[-1]:
    cnt = 0
    for ip in net:
        ip = f'{ip:b}'
        if ip.count('1') % 5:
            cnt += 1
    print('Ответ:', cnt)
