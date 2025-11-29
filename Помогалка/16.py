a=int(input())
m=0
while a!=0:
    if a<10 or a%3==0:
        m+=1
    a=int(input())
print(m)