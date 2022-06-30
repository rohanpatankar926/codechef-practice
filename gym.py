# Chef has decided to join a Gym in ChefLand and if possible, also hire a personal trainer at the gym. The monthly cost of the gym is XX and personal training will cost him an additional YY per month. Chef's total budget per month is only ZZ. Print 1 if Chef can only join the gym, 2 if he can also have a personal trainer, and 0 if he can't even join the gym.

# Note that if Chef wants to hire a personal trainer, he must join the gym — he cannot hire the trainer without joining the gym.

t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if(x+y<=z):
        print("2")
    elif(x<=z):
        print("1")
    else:
        print("0")
        