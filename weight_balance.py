# No play and eating all day makes your belly fat. This happened to Chef during the lockdown. His weight before the lockdown was w_1w 
# 1
# ​
#   kg (measured on the most accurate hospital machine) and after MM months of lockdown, when he measured his weight at home (on a regular scale, which can be inaccurate), he got the result that his weight was w_2w 
# 2
# ​
#   kg (w_2 \gt w_1w 
# 2
# ​
#  >w 
# 1
# ​
#  ).

# Scientific research in all growing kids shows that their weights increase by a value between x_1x 
# 1
# ​
#   and x_2x 
# 2
# ​
#   kg (inclusive) per month, but not necessarily the same value each month. Chef assumes that he is a growing kid. Tell him whether his home scale could be giving correct results.

t=int(input())
for test_case in range(t):
    w1,w2,x1,x2,m=map(int,input().split(' '))
    weight=w2-w1
    case1=x1*m
    case2=x2*m
    if (weight>=case1 and case2>=weight):
        print (1)
    else:
        print (0)