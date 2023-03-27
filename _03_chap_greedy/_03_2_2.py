n,m,k = map(int,input().split())#n은 입력받은 data의 수, m은 총 몇번 더해야 하는지, k는 같은 수 연속 최고 횟수
data = list(map(int,input().split()))

data.sort()  #입력받은 수를 정렬한다.
first = data[n-1]  #가장 큰 수 
second= data[n-2]   #두번째로 큰 수 

#가장 큰 수가 더해지는 횟수 계산
count = (m//(k+1))*k #6665가 반복됨(k+1), m은 전체 리스트 횟수, 6665 두번 반복, 6이 세번 반복 되므로 k(3)을 곱함, count =6
count += m%(k+1)   #나머지 있을 경우

result =0
result += (count) *first   #가장 큰 수 6번 더하기
result += (m-count)*second  #두번째로 큰 수 두번 더하기

print(result)

