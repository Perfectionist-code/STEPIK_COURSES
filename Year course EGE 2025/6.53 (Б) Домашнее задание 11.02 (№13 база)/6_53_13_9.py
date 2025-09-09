from ipaddress import ip_network

ip_host = '133.57.64.130'
ip_net = '133.57.64.0'

cnt = 0
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if str(net.network_address) == ip_net:
        cnt += 1
print('Ответ:', cnt)