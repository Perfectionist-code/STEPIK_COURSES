import json

with open('group_people.json') as file:
    d = json.load(file)

# print(d)
max_cnt = 0
for group in d:
    cnt_women = 0
    for item in group['people']:
        if item['gender'] == 'Female' and item['year'] > 1977:
            cnt_women += 1
    if cnt_women > max_cnt:
        max_cnt = cnt_women
        res = (group['id_group'], max_cnt)
    print(group['id_group'], cnt_women)
print(*res)



