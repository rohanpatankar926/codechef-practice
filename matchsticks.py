t = int(input())
while t>0:
    #n = int(input())
    n,d = map(int,input().split())
    d1={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
    ans=n+d
    l=len(str(ans))
    ans=str(ans)
    count=0
    for i in range(l):
        count+=d1[int(ans[i])]
    print(count)
    t -= 1