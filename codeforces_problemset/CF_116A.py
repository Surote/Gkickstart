n=int(input())
maxcap=0
ontram=0
for stop in range(n):
    a,b = map(int,input().split())
    if stop == 0:
        maxcap=b
        ontram=b
        continue
    elif ontram-a+b>maxcap:
        maxcap=ontram-a+b
    ontram=ontram-a+b
print(maxcap)
    