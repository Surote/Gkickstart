n=int(input())
for i in range(n):
    x=int(input())
    if x<9:
        print(0)
    elif x==9:
        print(1)
    elif str(x)[-1] == '9':
        print(int(str(x)[:-1])+1)
    else:
        print(str(x)[:-1])