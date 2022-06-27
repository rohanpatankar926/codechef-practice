# Chef has to travel to another place. For this, he can avail any one of two cab services.

# The first cab service charges XX rupees.
# The second cab service charges YY rupees.
# Chef wants to spend the minimum amount of money. Which cab service should Chef take?

t=int(input())
for tc in range(0,t):
  (x,y)=[int(i) for i in input().split()]
  if x<y:
    print("first")
  elif(x>y):
    print("second")
  else:
    print("any")