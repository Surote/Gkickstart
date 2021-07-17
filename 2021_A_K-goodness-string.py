for testcase in range(int(input())):
    n,k = map(int,input().split())
    n=n-1
    strk = input()
    check=0
# si < sn-i-1
    for i in range((len(strk)+1)//2):
        if strk[i] != strk[n-i]:
            #print(strk[i],strk[n-i],i,n-i)
            check+=1
    print('Case #'+str(testcase+1)+': '+str(abs(check-k)))
    