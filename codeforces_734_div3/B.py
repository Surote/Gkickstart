t=int(input())
alpha='abcdefghijklmnopqrstuvwxyz'
for i in range(t):
    morethan2 = []
    less=[]
    strk=input()
    for k in alpha:
        if k in strk:
            countstrk = strk.count(k)
            if countstrk >=2:
                morethan2.append(k)
            else:
                less.append(k)
    #print(morethan2,less)
    print(len(morethan2)+len(less)//2)
            
        
        
