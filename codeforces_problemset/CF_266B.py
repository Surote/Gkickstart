n,t=map(int,input().split())
strk=input()
strk=strk+"X"
strk_list=[]
for i in range(len(strk)):
    strk_list.append(strk[i])
for i in range(t):
    flag=0
    for s in range(len(strk_list)):
        if flag==1:
            flag=0
            continue
        if strk_list[s] == 'B' and strk_list[s+1] == 'G':
            strk_list[s] = 'G'
            strk_list[s+1] = 'B'
            flag=1
print("".join(strk_list)[:-1])
            

