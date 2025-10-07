from ipaddress import ip_network

for A in range(255, 0, -1):
    try:
        net = ip_network(f'176.112.100.128/255.255.255.{A}', 0)
        if net.num_addresses == 16:
            print('Ответ:', A)
            break
    except ValueError:
        continue
