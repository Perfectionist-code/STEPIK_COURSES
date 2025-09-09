from ipaddress import ip_network

ip_host = '218.194.82.148'
mask = '255.255.255.192'
net = ip_network(f'{ip_host}/{mask}', 0)
print(net, net.num_addresses)
temp = str(net).rsplit('.')
temp[-1] = str(int(temp[-1].split('/')[0]) + net.num_addresses - 2)
max_host_ip = ''.join(temp)
print('Ответ:', max_host_ip)
