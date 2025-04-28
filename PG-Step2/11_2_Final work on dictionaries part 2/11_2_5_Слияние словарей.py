def merge(dict_lst):      # values - это список словарей
     res_dict = {}
     for _dict in dict_lst:
          for key, value in _dict.items():
               if key not in res_dict:
                    res_dict.setdefault(key, {value})
               else:
                    res_dict.get(key).add(value)
     return  res_dict



# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
result = merge([{}, {}, {}])

print(result)


# def merge(values):
#     res = {}
#     for d in values:
#         for k, v in d.items():
#             res.setdefault(k, set()).add(v)
#     return res