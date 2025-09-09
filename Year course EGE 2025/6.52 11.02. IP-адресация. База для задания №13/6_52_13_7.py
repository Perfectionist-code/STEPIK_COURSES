from ipaddress import ip_network

ip_host = '158.116.11.164'
ip_net = '158.116.0.0'

cnt = 0
for mask in range(33):
    net = str(ip_network(f'{ip_host}/{mask}', 0))
    if net.startswith(ip_net):
        cnt += 1
print('Ответ:', cnt)
