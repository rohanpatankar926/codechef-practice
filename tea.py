t=int(input())
for i in range(0,t):
    a= list(map(int,input().strip().split()))
    q=a[0]//a[1]
    r=a[0]%a[1]
    if (q==0 and r==0):
        print(a[2])
    elif (q!=0 and r==0):
        print(q*a[2])
    else:
        print((q+1)*a[2])