strk = input()
upper=0
lower=0
for i in strk:
    if i == i.upper():
        upper+=1
    else:
        lower+=1
if lower>=upper:
    print(strk.lower())
else:
    print(strk.upper())