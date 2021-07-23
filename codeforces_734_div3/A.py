t=int(input())
for i in range(t):
    n=int(input())
    a=n//3
    b=a+1
    if n%3==0:
        print(a,a)
    elif a+2*b == n:
        print(a,b)
    else:
        print(a+1,a)