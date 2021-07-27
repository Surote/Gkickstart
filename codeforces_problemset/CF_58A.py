hello='hello'
s=input()
count=0
markhello=0
mark=0
while markhello<len(hello) and mark<len(s):
    if markhello==5:
        break
    if s[mark]==hello[markhello]:
        markhello+=1
    mark+=1
print('YES') if markhello==5 else print('NO')