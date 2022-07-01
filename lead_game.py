t=int(input())
player1=0
player2=0
lead=0
for test_case in range(t):
    score1,score2=map(int,input().split(' '))
    player1+=score1
    player2+=score2
    score_difference=player1-player2
    if score_difference>0 and score_difference>lead:
        lead=score_difference
        leader=1
    elif score_difference<0 and abs(score_difference)>lead:
        lead=abs(score_difference)
        leader=2
print(leader,lead)