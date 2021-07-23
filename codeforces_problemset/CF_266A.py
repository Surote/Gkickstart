n=input()
strk=input()
strk=strk+'#'
count=0
for i in range(len(strk)-1):
    if strk[i]==strk[i+1]:
        count+=1
print(count)
