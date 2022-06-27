# Chef's son wants to go on a roller coaster ride. The height of Chef's son is XX inches while the minimum height required to go on the ride is HH inches. Determine whether he can go on the ride or not.

t=int(input())
for test_case in range(t):
    (x,h)=map(int,input().split(' '))
    if x>=h:
        print("Yes")
    else:
        print("No")