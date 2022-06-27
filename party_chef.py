# Chef wants to give a burger party to all his NN friends i.e. he wants to buy one burger for each of his friends.

# The cost of each burger is XX rupees while Chef has a total of KK rupees.

# Determine whether he has enough money to buy a burger for each of his friends or not.

t=int(input())
for test_case in range(t):
    (x)=input().split(' ')
    total_cost=int(x[0])*int(x[1])
    if (total_cost<=int(x[2])):
        print("yes")
    else:
        print("no")