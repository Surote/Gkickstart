n,k = map(int,input().split())
while k!=0:
    if str(n)[-1] == '0':
        n = str(n)[:-1]
    else:
        n = str(int(n)-1)
    k-=1
print(n)
