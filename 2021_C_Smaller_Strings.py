MOD =10**9+7

def solve(n,k,strk):
    #print(n//2+1)
    if n%2==0:
        mid = n//2
    else:
        mid = n//2+1
    sumx = 0
    for i in range(mid):
        x = ord(strk[i])-ord('a')
        sumx += x*pow(k,mid-i-1,MOD)
    if n%2==0:
        if strk[:mid]+strk[:mid][::-1] < strk:
            sumx+=1
    else:
        if strk[:mid]+strk[:mid-1][::-1] < strk:
            sumx+=1
    return sumx


if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        n,k = list(map(int,input().split()))
        strk = input()
        sumx = solve(n,k,strk)
        print('Case #'+str(i+1)+': '+str(sumx%MOD))