a=int(input())
temp=[int(x) for x in input().split()]

count=0
dict={1:0,2:0,3:0,4:0}
for i in temp:
    dict[i]+=1
count+=dict[4]

if dict[3]:
    temp=min(dict[3],dict[1])
    count+=temp
    dict[1]-=temp
    dict[3]-=temp

if dict[2]:
    count+=dict[2]//2
    dict[2]-=((dict[2]//2)*2)

if dict[1] and dict[2]:
    temp=min(dict[2],dict[1])
    count+=temp
    dict[1]-=temp*2
    dict[2]-=temp

if dict[1]:
    temp+=dict[1]//4
    dict[1]-=((dict[1]//4)*4)
count=count+dict[1]+dict[2]+dict[3]
print(count)