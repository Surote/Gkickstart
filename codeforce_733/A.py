for testcase in range(int(input())):
    num = str(input())
    if len(num) == num.count('1')+num.count('0'):
        print('1')
    else:
        maxnum=1
        for i in range(len(num)):
            if num[i]!='0' and num[i]!='1' and int(num[i])>maxnum:
                maxnum=int(num[i])

        print(maxnum)
                