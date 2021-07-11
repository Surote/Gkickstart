n = int(input())
ln = []
ans = []
for i in range(n):
    maxpos = 0
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
 
    ln.append(a)
    ln.append(b)
    ln.append(c)
    callist = []
    # row1
    if 2*a[1] == a[0]+a[2]:
        maxpos+=1
    # row3
    if 2*c[1] == c[0]+c[2]:
        maxpos+=1
    # col1
    if 2*b[0] == a[0]+c[0]:
        maxpos+=1
    # col3
    if 2*b[1] == a[2]+c[2]:
        maxpos+=1
    if (a[0]+c[2])%2 == 0:
        callist.append((a[0]+c[2])/2)
    if (a[2]+c[0])%2 == 0:
        callist.append((a[2]+c[0])/2)
    if (b[0]+b[1])%2 == 0:
        callist.append((b[0]+b[1])/2)
    if (a[1]+c[1])%2 == 0:
        callist.append((a[1]+c[1])/2)
    print('Case #'+str(i+1)+': '+str(len(callist)-len(set(callist))+1+maxpos))