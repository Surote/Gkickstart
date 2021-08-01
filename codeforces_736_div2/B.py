t=int(input())
for i in range(t):
    n=int(input())
    ffrow=input()
    ssrow=input()
    ffrow='x'+ffrow+'x'
    ssrow='x'+ssrow+'x'
    frow=[]
    srow=[]
    for k in range(len(ffrow)):
        frow.append(ffrow[k])
        srow.append(ssrow[k])
    count=0
    for j in range(1,len(srow)-1):
        if srow[j] =='1' and (frow[j]=='1'or frow[j]=='2') and frow[j-1]=='1':
            count+=1
            frow[j-1]='2'
            #frow=frow[:j-1]+'2'+frow[j:]
        elif srow[j] =='1' and (frow[j]=='1'or frow[j]=='2')  and frow[j+1]=='1':
            count+=1
            frow[j+1]='2'
            #frow=frow[:j+1]+'2'+frow[j+2:]
        elif srow[j]=='1' and frow[j]=='2' and frow[j-1]=='1':
            count+=1
            frow[j-1]='2'
            #frow=frow[:j-1]+'2'+frow[j:]
        elif srow[j]=='1' and frow[j]=='2' and frow[j+1]=='1':
            count+=1
            frow[j+1]='2'
        elif srow[j] == '1' and frow[j]=='0':
            count+=1
            frow[j]='2'
           # frow=frow[:j]+'2'+frow[j+1:]
        
        #print(frow)
    print(count)

