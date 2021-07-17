# k-k//4
import math
for testcase in range(int(input())):
    nstages = int(input())
    yourscore = list(map(int,input().split()))
    ilyascore = list(map(int,input().split()))
    yourscore = sorted(yourscore)
    ilyascore = sorted(ilyascore)
    #print(nstages,yourscore,ilyascore)
    scoreuse = nstages-(nstages//4)
    #print(sum(yourscore[len(yourscore)-scoreuse:]) , sum(ilyascore[len(ilyascore)-scoreuse:]))
    if sum(yourscore[len(yourscore)-scoreuse:]) > sum(ilyascore[len(ilyascore)-scoreuse:]):
        print('0')
    else:
        '''
        count=0
        while sum(yourscore[len(yourscore)-scoreuse:]) < sum(ilyascore[len(ilyascore)-scoreuse:]):
            
            count+=1
            # increase additional by 1
            nstages=nstages+1
            yourscore.append(100)
            ilyascore.insert(0,0)
            scoreuse = nstages-(nstages//4)
        '''
        maxilya = sum(ilyascore)
        print(math.ceil((maxilya-sum(yourscore[len(yourscore)-scoreuse:]))/100))
        #    print(scoreuse,yourscore,ilyascore,nstages,count)
        #    print(sum(yourscore[len(yourscore)-scoreuse:]) , sum(ilyascore[len(ilyascore)-scoreuse:]))
        #print(count)
            



    