testcase = int(input())
for num in range(testcase):
    n = int(input())
    # find max n
    if n==1 or n==2:
        print('Case #'+str(num+1)+': 1')
        continue
    maxn=0 
    sumn =0
    while sumn < n:
        sumn+=maxn
        maxn+=1

    #print(maxn)
    count = 0
    for i in range(1,n):
        isint = (2*n-i*(i-1))
        if isint % (2*i)==0 and i<maxn:
            #print(isint/(2*i),i)
            count+=1
        if i>maxn:
            break
    print('Case #'+str(num+1)+': '+str(count))