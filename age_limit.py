# Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

# Minimum age limit is XX (i.e. Age should be greater than or equal to XX).
# Age should be strictly less than YY.
# Chef's current Age is AA. Find whether he is currently eligible to take the exam or not.

t=int(input())
for test_case in range(t):
    (x,y,a)=map(int,input().split(' '))
    if a>=x and a<y:
        print("YES")
    else:
        print("NO")