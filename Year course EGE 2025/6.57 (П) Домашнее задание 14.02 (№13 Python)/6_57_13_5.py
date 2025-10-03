from  ipaddress import ip_network, ip_address

def condition(n) -> bool:
    for ip in n:
        ip = f'{ip:b}'
        if ip[16:24].count('0') <= ip[24:].count('0'):
            # print(ip)
            return False
    print(n.with_netmask)
    return True

cnt = 0
for A in range(0,256):
    ip_host = ip_address(f'246.81.65.{A}')
    net = ip_network(f'{ip_host}/255.255.255.224',0)
    # print(net.with_netmask)
    if net[0] < ip_host < net[-1] and condition(net):
        print(A)
        cnt += 1
print(cnt)