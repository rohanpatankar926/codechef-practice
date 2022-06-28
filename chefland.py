# In ChefLand, human brain speed is measured in bits per second (bps). Chef has a threshold limit of XX bits per second above which his calculations are prone to errors. If Chef is currently working at YY bits per second, is he prone to errors?

# If Chef is prone to errors print YES, otherwise print NO.

x,y=map(int,input().split(' '))
if x>y:
    print("No")
if x==y:
    print("No")
if x<y:
    print("Yes")
