n,m=map(int,input().split())
frdict={}
if m==0:
    for i in range(1,n+1):
        frdict[i]=[]
for fr in range(m):
    u,v=map(int,input().split())
    if u not in frdict:
        frdict[u]=[]
    if v not in frdict:
        frdict[v]=[]
    #print(frdict)
    frdict[u].append(v)
    frdict[v].append(u)
    #print(frdict)
    
q=int(input())
#print('a')
frtempdict=frdict.copy()
for qu in range(q):
    qn = input()
    #print(qn.split())
    if qn == '3':
        for kill in list(frtempdict):
            #print(kill)
            #if kill in list(frtempdict):
            if len(frtempdict[kill])!=0 and min(frtempdict[kill]) > kill:
                frtempdict.pop(kill,None)
            print(frtempdict)
            #for kill2 in frtempdict[kill]:
            #    if kill2 < kill:
            #        frtempdict.pop(kill2,None)
        print(len(frtempdict))
        frtempdict=frdict.copy()
                
    elif qn.split()[0]=='1':
        qn=list(map(int,qn.split()))
        if qn[1] in frtempdict:
            frtempdict[qn[1]].append(qn[2])
        else:
            frtempdict[qn[1]]=[]
            frtempdict[qn[1]].append(qn[2])
        if qn[2] in frtempdict:
            frtempdict[qn[2]].append(qn[1])
        else:
            frtempdict[qn[2]]=[]
            frtempdict[qn[2]].append(qn[1])

    else:
        #print(frtempdict)
        qn=list(map(int,qn.split()))
        if qn[1] in frtempdict:
            if qn[2] in frtempdict[qn[1]]:
                frtempdict[qn[1]].remove(qn[2])
        if qn[2] in frtempdict:
            if qn[1] in frtempdict[qn[2]]:
                frtempdict[qn[2]].remove(qn[1])

    #print(frdict)