# CodeChef recently revamped its practice page to make it easier for users to identify the next problems they should solve by introducing some new features:

# Recent Contest Problems - contains only problems from the last 2 contests
# Separate Un-Attempted, Attempted, and All tabs
# Problem Difficulty Rating - the Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience
# Popular Topics and Tags
# Like most users, Chef didn’t know that he could add problems to a personal to-do list by clicking on the magic '+' symbol on the top-right of each problem page. But once he found out about it, he went crazy and added loads of problems to his to-do list without looking at their difficulty rating.

# Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than 10001000. Given a list of difficulty ratings for problems in the Chef’s to-do list, please help him identify how many of those problems Chef should remove from his to-do list, so that he is only left with problems of difficulty rating less than 10001000.

t=int(input())
for test_case in range(t):
    n=int(input())
    count=0
    l=list(map(int,input().split()))
    for j in l:
        if j>999:
            count=count+1
    print(count)