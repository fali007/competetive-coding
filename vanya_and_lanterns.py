a,b=map(int,input().split(' '))
array=map(int,input().split(' '))
array=sorted(array)
max_gap=max(array[0],a-array[-1])
for i in range(1,len(array)):
    max_gap=max((array[i]-array[i-1])/2,max_gap)
print("%.9f"%(max_gap))