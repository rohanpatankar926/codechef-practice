# According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for XX weeks, and the cost of classes per week is YY coins. What is the total amount of money that Chef will have to pay?

t=int(input())
for test_case in range(t):
    (x,y)=map(int,input().split(' '))
    print(x*y)