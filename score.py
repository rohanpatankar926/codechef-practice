# Chef appeared for a placement test.

# There is a problem worth XX points. Chef finds out that the problem has exactly 1010 test cases. It is known that each test case is worth the same number of points.

# Chef passes NN test cases among them. Determine the score Chef will get.

# NOTE: See sample explanation for more clarity.

t=int(input())
for test_case in range(t):
    (x,y)=map(int,input().split(' '))
    print(int(x/10*y))