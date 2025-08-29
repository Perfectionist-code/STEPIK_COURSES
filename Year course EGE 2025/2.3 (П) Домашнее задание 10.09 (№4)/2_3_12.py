for Н in range(2, 11):
    for И in range(3, 11):
        for Е in range(И, 11):
            for З in range(Е, 11):
                if Н +И + Е + З == 13:
                    print('-------')
                    print(*'НИЕЗ')
                    print(Н, И, Е, З)
