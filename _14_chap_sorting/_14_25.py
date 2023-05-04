def solution(n,stages):
    user = len(stages)  #사용자 수 
    fail={}  #실패율
   
    stages.sort()
    for i in range(1,n+1):
           if user ==0:   #사용자가 없다면
                 fail[i]=0  #실패율도0이다.
           else:  #사용자가 존재한다면
                 #i가 1일때, stages에서 1의 개수를 센 후에 사용자의 수로 나눠 실패율을 구한다.
                 fail[i] = stages.count(i)/user   
                #1인 사용자의 수를 사용자 수에서 빼, 남은 사용자의 수를 구한다. 
                 user-= stages.count(i)
                      
    fail = sorted(fail,key = lambda x :fail[x],reverse=True) #실패율의 크기에 따라 실패율을 내림차순으로 정렬한다.   
    return fail

solution(5,[2,1,2,6,2,4,3,3])