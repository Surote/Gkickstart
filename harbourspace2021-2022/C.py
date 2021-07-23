n=int(input())
for i in range(n):
    scoreA=0
    scoreB=0
    scoreA2=0
    scoreB2=0
    strk=input()
    strk2=strk
    ans1=0
    for j in range(10):
        # even team
        if strk[j] == '?' and j%2==0:
            strk = strk[:j]+'1'+strk[j+1:]
        # odd team
        elif strk[j] == '?':
            strk = strk[:j]+'0'+strk[j+1:]
    for k in range(10):
        #count score
        if strk[k] == '1':
            if k%2==0:
                scoreA+=1
            else:
                scoreB+=1
        #print('cal',scoreA - scoreB , (10-k)/2)
        if scoreA - scoreB > (10-k)/2:
            ans1=k+1
            break
    if k == 9:
        ans1=10

    for x in range(10):
        # even team
        if strk2[x] == '?' and x%2==0:
            strk2 = strk2[:x]+'0'+strk2[x+1:]
        # odd team
        elif strk2[x] == '?':
            strk2 = strk2[:x]+'1'+strk2[x+1:]
    #print(strk2)
    for y in range(10):
        #count score
        if strk2[y] == '1':
            if y%2==0:
                scoreA2+=1
            else:
                scoreB2+=1
       # print('cal',scoreB2 - scoreA2 , (10-y)/2)
        if scoreB2 - scoreA2 >= (10-y)/2:
            ans2=y+1
            break
    if y == 9:
        ans2=10
    
            

        
        # even team


    print(min(ans1,ans2))

