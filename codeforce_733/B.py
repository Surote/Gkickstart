for testcase in range(int(input())):
    h,w = map(int,input().split())
    table =[]
    for i in range(h+2):
        table.append([])
        for j in range(w+2):
            table[i].append(0)
    #print(table)
    for i in range(1,h+1):
        for j in range(1,w+1):
            if i==1 or j==1 or i==h or j==w:
                #print(i,j)
                if table[i-1][j]!=1 and table[i][j-1]!=1 and table[i+1][j]!=1 and table[i-1][j-1]!=1 and table[i-1][j+1]!=1 and table[i+1][j-1]!=1 and table[i+1][j+1]!=1 and table[i][j+1]!=1:
                    #print(table,table[i][j-1],table[i][j])
                    table[i][j]=1
                    #print(table,table[i][j-1],table[i][j])
    #print(table)
    for i in range(1,h+1):
        print(('').join(map(str,table[i][1:-1])))
    print()
        

