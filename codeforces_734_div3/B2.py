from collections import Counter
t=int(input())
for i in range(t):
    ans=[]
    intlistcheck=[]
    n,k=map(int,input().split())
    intlist=list(map(int,input().split()))
    print(Counter(intlist))
    print(n,k)
    for j in intlist:
        intlistcheck.append(j)
        mincolor=0
        minlist=[]
        flag=0
        for m in range(1,k+1):
            if len(ans)!=0 and m not in ans:
                mincolor=m
                flag=1
                break
            else:
                mincolor=1
        #all number in ans
        if flag==0:
            for l in range(1,k+1):
                minlist.append(ans.count(l))
            mincolor=minlist.index(min(minlist))+1

        print(mincolor)

        if intlistcheck.count(j) == 1:
            ans.append(mincolor)
        elif intlistcheck.count(j) > k:
            ans.append(0)
            continue
        else:
            # if in inlistcheck

            usecolor=[]
            for pp in intlistcheck:
                if pp == j:
                    usecolor.append(ans[intlistcheck.index(pp)])
                    print(ans[intlistcheck.index(pp)])
            if mincolor not in usecolor:
                ans.append(mincolor)
                continue
            for kk in range(1,k+1):
                if kk not in usecolor:
                    ans.append(kk)
                    break
            
            
        
        
    print(intlist)
    print(ans,intlistcheck)
    #print((" ").join(ans))
