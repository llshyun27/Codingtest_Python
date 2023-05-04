#우선순위 큐는 원소를 넣었다 빼는 것만으로도 정렬된 결과를 얻을 수 있다.
import heapq
n = int(input())
#힙에 초기 카드 묶음을 모두 삽입
heap =[]
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)  #힙에 입력받은 data를 삽입한다. 
result =0
#힙에 원소가 1개 남을 때까지
while len(heap)!=1:
    #가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)  #가장 작은 값을 꺼내어 one에 저장
    two = heapq.heappop(heap)  #그 다음으로 작은 값을 꺼내어 two에 저장
    #카드 묶음을 합쳐서 다시 삽입
    sum_value = one+two  # 가장 작은 값 2개를 더한다. 
    result +=sum_value    #result에 이 더한 값을 넣고 계속 계산해 나간다. 
    heapq.heappush(heap,sum_value)   #힙에 더한 값을 넣는다. 

print(result)