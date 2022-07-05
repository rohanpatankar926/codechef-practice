for test_case in range(int(input())):
    (n,x,y)=map(int,input().split(' '))
    ans=x+(y*2)
    if ans<n:
        print("YES")
    elif ans>n:
        print("NO")
    if ans==n:
        print("YES")