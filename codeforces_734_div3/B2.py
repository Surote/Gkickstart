for _ in range(int(input())):
    n,k=map(int,input().split())
    num=list(map(int,input().split()))
    dic={}
    for i in range(n):
        if num[i] not in dic:
            dic[num[i]]=[]
        dic[num[i]].append(i)
    #print(dic)
    ans=[0]*n
    temp=[]
    for j in dic:
        for m in range(min(k,len(dic[j]))):
            temp.append(dic[j][m])
            if len(temp) == k:
               # print(temp)
                for fil in range(k):
                    ans[temp[fil]]=fil+1
                temp=[]
        #print(temp)

    print(*ans)