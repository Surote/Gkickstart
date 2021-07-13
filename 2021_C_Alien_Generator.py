testcase = int(input())
for i in range(testcase):
    n = int(input())
    count = 0
    for _ in range(1,n+1):
        sum_ = 0
        for j in range(_,n+1):
            sum_+=j
            if sum_ == n:
               # print(_,sum_)
                count+=1
            elif sum_ > n:
                break
    print('Case #'+str(i+1)+': '+str(count))
        