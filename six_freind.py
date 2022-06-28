# Six friends go on a trip and are looking for accommodation. After looking for hours, they find a hotel which offers two types of rooms — double rooms and triple rooms. A double room costs Rs. XX, while a triple room costs Rs. YY.

# The friends can either get three double rooms or get two triple rooms. Find the minimum amount they will have to pay to accommodate all six of them.

t=int(input())
for test_case in range(t):
    #x-->double bed room cost
    #y-->triple bed room cost
    (x,y)=map(int,input().split(' '))
    if (x*3<=y*2):
        print(x*3)
    else:
        print(y*2)
    