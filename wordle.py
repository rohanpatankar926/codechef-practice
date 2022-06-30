# Chef invented a modified wordle.

# There is a hidden word SS and a guess word TT, both of length 55.

# Chef defines a string MM to determine the correctness of the guess word. For the i^{th}i 
# th
#   index:

# If the guess at the i^{th}i 
# th
#   index is correct, the i^{th}i 
# th
#   character of MM is \texttt{G}G.
# If the guess at the i^{th}i 
# th
#   index is wrong, the i^{th}i 
# th
#   character of MM is \texttt{B}B.
# Given the hidden word SS and guess TT, determine string MM.

t=int(input())
for test_case in range(t):
    s=input()
    t=input()
    m=''
    for i in range(len(s)):
        if s[i]==t[i]:
            m+="G"
        else:
            m+="B" 
    print(m)        
    