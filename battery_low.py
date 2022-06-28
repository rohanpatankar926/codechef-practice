# Chef's phone shows a Battery Low notification if the battery level is 15 \%15% or less.

# Given that the battery level of Chef's phone is X \%X%, determine whether it would show a Battery low notification.

t=int(input())
for test_case in range(t):
    x=int(input())
    if x>15:
        print("No")
    else:
        print("Yes")