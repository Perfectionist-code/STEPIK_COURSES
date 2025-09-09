from ipaddress import ip_network

ip_host = '76.155.48.2'
ip_net = '76.155.48.0'

cnt = 0
for mask in range(33):
    net = str(ip_network(f'{ip_host}/{mask}', 0))
    if net.startswith(ip_net):
        cnt += 1
print('Ответ:', cnt)
