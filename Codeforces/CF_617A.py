n = int(input())
ans  =0 
for i in range(5,0,-1):
    #print("N: ",n)
    if n%i==0:
        #print("N div i: ",n//i,i)
        ans+=n//i
        break
    else:
        #print(n//i,n%i,i)
        ans+=n//i
        n=n%i
print(ans)