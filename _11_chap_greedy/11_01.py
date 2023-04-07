#모험가 수 n명을 입력받는다.
n = int(input())

#각 모험가의 공포도 값을 n 이하로 입력받는다.
fear = list(map(int,input().split()))

# 총 그룹의 수를 알려줄 변수를 설정한다.
group = int(0)

# 해당 공포도에 몇명이 있는지 알려줄 변수를 설정한다. 
result = int(0)

#for 반복문과 if를 사용해 공포도의 값을 한명씩 검사한후 더한다.
for i in range(1,n+1):
    for j in range(0,n):
        if i == fear[j]:
            result+=1     #i의 값과 fear 리스트에 들어있는 공포도가 같으면 result에 1을 더한다. 
    if i<=result:   #result(해당 공포도에 몇명이 있는지)가 i보다 크거나 같은 경우
       group+=1     # 그룹에 1을 더하여 여행을 떠날 수 있는 그룹의 수를 추가한다.
       result = int(0)   #result값을 다시 0으로 재설정한다. 

print(group)   #여행을 떠날 수 있는 그룹의 수를 추가한다. 
    


