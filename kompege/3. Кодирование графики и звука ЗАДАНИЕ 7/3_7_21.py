sp1 = 2 ** 20
sp2 = 2 ** 13
V = 10 * 2 ** 23
v_start = 1024 * 2 ** 13
t_start_upload = v_start // sp1
t_download = V // sp2
t_total = t_download + t_start_upload
print('Ответ', t_total)

