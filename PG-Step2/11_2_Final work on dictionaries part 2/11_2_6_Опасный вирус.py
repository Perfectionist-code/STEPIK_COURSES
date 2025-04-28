d = {'W': 'write',
     'R': 'read',
     'X': 'execute'}
d_req = {value: key for key, value in d.items()}
files_dict = {file_name: requests for file_name, *requests in (input().split() for _ in range(int(input())))}
requests_lst = [input().split() for __ in range(int(input()))]
for request, file_name in requests_lst:
     print(('Access denied', 'OK')[d_req[request] in files_dict[file_name]])








