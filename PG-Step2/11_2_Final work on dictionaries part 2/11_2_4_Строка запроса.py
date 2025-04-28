def build_query_string(params):
     d = params
     request = []
     for key, value in d.items():
          request.append(f'{key}={value}')
     request.sort()
     return '&'.join(request)
