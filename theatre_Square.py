inp=input().split(' ')
m=int(inp[0])
n=int(inp[1])
a=int(inp[2])
if a>m or a>n:
    if a*a>m*n:
        print(1)
    else:
        print(max(m,n))
else:
    div1=m//a
    div2=n//a
    ans=div1*div2
    if m%a:
        ans+=(div2)
    if n%a:
        ans+=(div1)
    if m%a and n%a:
        ans+=1
    print(ans)