a,b=map(int,input().split())
sums=a
tod = 0
while b<=a:
#  print a,sums
  #print(a,sums)
  sums+=a//b
  if a%b!=0:
    tod+=a%b
    a=a//b + tod
  else:
    a=a//b
  #print(tod)
  tod=0
print(sums+(tod+a)//b)