from ipaddress import ip_network
ip_host = '111.81.208.27'
ip_net =  '111.81.192.0'

for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    print(net, net.netmask)
    if str(net).startswith(ip_net):
        print('-----' * 10)
        print(net.netmask)
        print('Ответ:', str(net.netmask).split('.')[-2])
        break
