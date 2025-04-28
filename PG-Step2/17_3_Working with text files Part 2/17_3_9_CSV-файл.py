def read_csv():
    with open('data.csv') as file:
        line = file.readline().strip()
        d = [key for key in line.split(',')]
        res_lst= []
        for line in file:
            line = line.strip().split(',')
            res_lst.append(dict(zip(d,line)))
        return res_lst
#         print(res_lst)
#
#
# read_csv()
