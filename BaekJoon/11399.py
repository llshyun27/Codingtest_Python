# ATM 앞에 사람들이 줄을 서있다. 각 사람마다 필요한 시간을 입력받고
# 모든 사람들이 돈을 인출하는데 필요한 시가의 합의 최솟값을 구하여라
#예시
# 5
# 3 1 4 3 2 -> 1 2 3 3 4 
# total[0] = 1
# total[1] = 1+2
# total[2] = 1+2+3
# total[3] = 1+2+3+3
# total[4] = 1+2+3+3+4  후에 total[0]~total[4]까지 더한다.

n = int(input())    # 총 사람의 수를 입력받는다.
time = list(map(int,input().split())) #각 사람이 필요한 시간을 입력받는다.
time.sort()  #최솟값을 구하기 위해 시간을 오름차순으로 정렬한다.

total = list(range(n)) #더한 값을 저장할 리스트를 만든다. 
total[0] = time[0]
count = int(0)
i = int(1)
while i<n:
      total[i] = total[i-1]+time[i]  #더한값을 total에 저장한다.
      i +=1

print(sum(total))  #total리스트에 있는 모든 값을 더한것을 출력한다. 