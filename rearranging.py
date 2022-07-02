for test_case in range(int(input())):
    d=int(input())
    n=float(input())
    list_=[]
    for i in range(d):
        number=n%10
        list_.append(number)
        n=n//10
    found=False
    for j in range(d):
        if list_[j]==0 or list_[j]==5:
            found=True
            break
    if found==True:
        print("Yes")
    else:
        print("No")