# Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly XX minutes.

# The meeting platform supports a meeting of maximum 3030 minutes without subscription and a meeting of unlimited duration with subscription.

# Determine whether Chef needs to take a subscription or not for setting up the meet.

t=int(input())
for test_case in range(t):
    x=int(input())
    if x>30:
        print("Yes")
    else:
        print("No")