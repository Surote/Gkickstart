n=int(input())
if n%2==0:
    print(int(pow(n/2,2)*(-1)+(n/2)*((n/2)+1)))
else:
    print(int(pow((n//2)+1,2)*(-1)+(n//2)*((n//2)+1)))