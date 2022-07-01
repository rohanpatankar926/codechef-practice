for i in range(int(input(""))):
    n = int(input())
    arr2=list(map(int, input().split(" ")))
    arr2.sort()
    print(arr2)
    a=0
    max=0
    for j in range(n-1):
        if arr2[j]==arr2[j+1]:
            a+=1
        else:
            if max<a:
                max=a
                print(f"max is {max}")
            a=0
    if a>0 and a>max:
        max = a
    print(max)
    print(n-max-1)