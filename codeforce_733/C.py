
for testcase in range(int(input())):
    nstages = int(input())
    yourscore = list(map(int,input().split()))
    ilyascore = list(map(int,input().split()))
    yourscore = sorted(yourscore)
    ilyascore = sorted(ilyascore)
    #print(nstages,yourscore,ilyascore)
    scoreuse = nstages//4
    #print(sum(yourscore[len(yourscore)-scoreuse:]) , sum(ilyascore[len(ilyascore)-scoreuse:]))
    prefixscore1 = sum(yourscore[scoreuse:])
    prefixscore2 = sum(ilyascore[scoreuse:])
    if prefixscore1 >= prefixscore2:
        print(0)
    else:
        count=0
        p1 = scoreuse
        p2 = scoreuse-1
        print(p1,p2)
        while prefixscore1 < prefixscore2:
            count+=1
            nstages+=1
            #print('BE',nstages,nstages-nstages//4,prefixscore1,prefixscore2)
            if p2 >= 0 and nstages%4!=0:
                prefixscore2+=ilyascore[p2]
                p2-=1
            if nstages%4==0 and p1<len(yourscore):
                prefixscore1-=yourscore[p1]
                p1+=1
            elif p1<=len(yourscore) and nstages%4==0:
                prefixscore1-=100
            prefixscore1+=100
            #print('AF',nstages,nstages-nstages//4,prefixscore1,prefixscore2)
            
        
        #    print(scoreuse,yourscore,ilyascore,nstages,count)
        #    print(sum(yourscore[len(yourscore)-scoreuse:]) , sum(ilyascore[len(ilyascore)-scoreuse:]))
        print(count)
            



    