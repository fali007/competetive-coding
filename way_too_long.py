a=int(input())
list=[]
for _ in range(a):
    list.append(input())
ans=[]
for i in range(len(list)):
    if len(list[i])>10:
        list[i]=list[i][0]+str(len(list[i])-2)+list[i][-1]
for i in list:
    print(i)