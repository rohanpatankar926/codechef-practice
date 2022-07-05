for test_case in range(int(input())):
    (k,x)=map(int,input().split(' '))
    #k-->capacity of k litres
    #x--already filled with water
    ans=k-x
    print(ans)