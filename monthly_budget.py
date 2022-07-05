for test_case in range(int(input())):
    a,b=map(int,input().split(' '))
    mul=30*b
    if a>mul:
        print("YES")
    elif a<mul:
        print("NO")
    elif a==mul:
        print("YES")
    else:
        print("NO")