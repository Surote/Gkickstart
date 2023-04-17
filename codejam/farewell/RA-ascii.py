import math
t=input()
li=[]
al=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(int(t)):
    su=""
    cal=0
    c=1
    n=int(input())
    while cal < n:
        cal+=26*c
        c+=1
   # print(cal-c*26,c)
    c=c-1
   # print(c)
    for k in al:
        su+=k*c
    #print(su,su[n-(cal-c*26)+1])
    print("CASE #"+str(i+1)+": "+str(su[n-(cal-c*26)-1]))
