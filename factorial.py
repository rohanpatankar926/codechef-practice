def factorial(n):
    if n<0:
        print("Please enter value >1")
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
    
t=int(input())
for test_case in range(t):
    n=int(input())
    print(factorial(n))
    