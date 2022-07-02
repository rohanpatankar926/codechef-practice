for test_case in range(int(input())):
    n=(input())
    if n==n[::-1]:
        print("wins")
    else:
        print("loses")