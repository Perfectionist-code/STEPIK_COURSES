from ipaddress import ip_network

ip_host = '173.103.25.118'
ip_net = '173.103.24.0'

res_mask = None
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if (net_s := str(net)).startswith(ip_net):
        res_mask = int(net_s.split('/')[-1])
        break
print('Ответ:', 32 - res_mask)
