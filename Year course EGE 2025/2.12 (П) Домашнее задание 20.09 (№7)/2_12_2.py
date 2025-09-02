k_A = k_B = 2
nu_A = 66_000
i_A = 32
nu_B = 44_000
i_B = 16
v_B = 11 * 2 ** 23
t = v_B * 12 / (k_B * i_B * nu_B)
v_a = k_A * nu_A * i_A * t
print('Ответ:', int(v_a / (2 * 2 ** 23)), 'Мб')

# print('Ответ:', int(nu2 / 1000), 'кГц')
