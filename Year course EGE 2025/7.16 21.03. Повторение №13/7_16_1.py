from ipaddress import ip_network

for oct in range(255, 1, -1):
    try:
        net = ip_network(f'176.112.100.128/255.255.255.{oct}', 0)
        if net.num_addresses == 16:
            print(oct)
            break
    except ValueError:
        continue
