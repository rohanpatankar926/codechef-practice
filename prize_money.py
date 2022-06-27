# In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:

# Top 1010 participants receive rupees XX each.
# Participants with rank 1111 to 100100 (both inclusive) receive rupees YY each.


t=int(input())
for test_case in range(t):
    (x,y)=map(int,input().split(' '))
    total_prize_money=10*x+90*y
    print(total_prize_money)