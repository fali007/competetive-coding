k=3
a=[]
l=1
for i in range(k):
    temp=[]
    for _ in range(2**i):
        temp.append(l)
        l+=1
    a.append(temp)
for i in range(k-1):
    array=a[len(a)-1]
    temp=[]
    j=0
    while j<len(array):
        temp.append(array[j]+array[j+1])
        j+=2
    a.append(temp)
print(a)