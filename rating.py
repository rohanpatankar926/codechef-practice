# Chef's current rating is XX, and he wants to improve it. It is generally recommended that a person with rating XX should solve problems whose difficulty lies in the range [X, X+200][X,X+200], i.e, problems whose difficulty is at least XX and at most X+200X+200.

# You find out that Chef is currently solving problems with a difficulty of YY.

# Is Chef following the recommended practice or not?

t=int(input())
for test_case in range(t):
    (x,y)=map(int,input().split(' '))
    if (x<=y and y<=x+200):
        print("Yes")
    else:
        print("No")