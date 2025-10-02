from ipaddress import ip_network, ip_address
def cond(n) -> bool:
    for ip in n:
        ip = f'{ip:b}'
        if ip[:16].count('1') < ip[16:].count('1'):
            return False
    return True



ip_host = ip_address('127.63.67.1')
for A in range(1,255):
    try:
        net = ip_network(f'{ip_host}/255.255.{A}.0',0)
        if net[0] < ip_host < net[-1] and cond(net):
            print('Ответ:', A)
            break
    except:
        continue
