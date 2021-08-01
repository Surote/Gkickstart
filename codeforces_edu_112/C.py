t=int(input())
for case in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    alllist=[a,b]
    posi=0
    posj=0
    while not (posj==n-1 and posi!=1):
        print(posi,posj)
        if posi == 0:
            if alllist[posi][posj+1] > alllist[posi+1][posj]:
                posj+=1
                print(alllist[posi][posj])
            else:
                posi+=1
                print(alllist[posi][posj])
        else:
            if alllist[posi][posj+1] > alllist[posi-1][posj]:
                posj+=1
                print(alllist[posi][posj])
            else:
                posi-=1
                print(alllist[posi][posj])
        print(posi,posj)
