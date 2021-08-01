

t=int(input())
for i in range(t):
    n=int(input())
    if n <=6:
        print(15)
    elif n <=8:
        print(20)
    elif n <=10:
        print(25)
    elif n%2==0:
        print(5*n/2)
    else:
        print(5*(n+1)/2)
