n=int(input())
array=[]
for _ in range(n):
    temp=input().split(' ')
    temp1=[]
    for i in temp:
        temp1.append(int(i))
    array.append(temp1)
count=0
for i in array:
    s=sum(i)
    if s>=2:
        count+=1
print(count)