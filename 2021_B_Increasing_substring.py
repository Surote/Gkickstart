testcase = int(input())
for test in range(testcase):
    n = int(input())
    s = input()
    #print(s)
    s = s+'z'
    anslist = []
    count = 1
    for i in range(len(s)-1):
        anslist.append(count)
        if s[i+1] > s[i]:
            count+=1
        else:
            count=1
    ansstr=""
    for ans in anslist:
        ansstr = ansstr+str(ans)+' ' 
    print('Case #'+str(test+1)+': '+ansstr)