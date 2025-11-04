from ipaddress import ip_network, ip_address

ip_host1 = ip_address('176.213.225.119')
ip_host2 = ip_address('176.213.195.58')
res = []
for mask in range(32, 15, -1):
    net1 = ip_network(f'{ip_host1}/{mask}', 0)
    net2 = ip_network(f'{ip_host2}/{mask}', 0)
    if net1 == net2:
        # print(net1.with_netmask)
        hosts = list(net1.hosts())
        if ip_host1 in hosts and ip_host2 in hosts:
            cnt = 0
            for ip in net1:
                ip = f'{ip:b}'
                if not ip.count('1') % 2:
                    cnt +=1
            res.append(cnt)
print(min(res), res)
