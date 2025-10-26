from ipaddress import ip_address, ip_network

# net = ip_network('167.66.136.176/255.254.0.0', 0)
#
# cnt = 1
# for ip in net:
#     if net[0] < ip < net[-1]:
#         print(f'{cnt}. {ip}', sum(map(int, str(ip).split('.'))))
#         cnt += 1
#     if cnt == 10:
#         break
#
# # ОТВЕТ 234 1час 49 мин

print(min(ip_network('167.66.136.176/255.254.0.0', 0).hosts()))