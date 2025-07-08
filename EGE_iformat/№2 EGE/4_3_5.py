d = {'Розовое': 'Белые',
     'Красное': 'Черные',
     'Синее': 'Голубые'}
choice_girls = (input(), input())
if 'Розовое' not in choice_girls:
    print(d['Розовое'])
elif 'Красное' not in choice_girls:
    print(d['Красное'])
else:
    print(d['Синее'])
