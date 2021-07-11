n = int(input())
ln = []
ans = []
for i in range(n):
    maxofarth=0
    maxj=0
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    mmax = max(max(a),max(b),max(c))
    mmin = min(min(a),min(b),min(c))
    
    ln.append(a)
    ln.append(b)
    ln.append(c)
    for j in range(mmin,mmax+1):
        # row1
        sumofath=0
        if a[1]-a[0] == a[2]-a[1]:
            sumofath+=1
        # row2
        if b[1]-j == j-b[0]:
            sumofath+=1
        # row3
        if c[1]-c[0] == c[2]-c[1]:
            sumofath+=1
        # col1
        if b[0]-a[0] == c[0]-b[0]:
            sumofath+=1
        # col2
        if j-a[1] == c[1]-j:
            sumofath+=1
        # col3
        if b[1]-a[2] == c[2]-b[1]:
            sumofath+=1
        # left diagonal
        if a[0]-j == j-c[2]:
            sumofath+=1
        # right diagonal
        if a[2]-j== j-c[0]:
            sumofath+=1
        if sumofath > maxofarth:
            maxofarth = sumofath
            maxj=j
    ans.append('Case #'+str(i+1)+': '+str(maxofarth))
    # print(ln,maxofarth,maxj)
for i in ans:
    print(i)