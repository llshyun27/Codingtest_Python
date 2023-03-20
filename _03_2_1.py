#n개의 정수, m번 더해서, k번 초과 더하기 금지
n,m,k =map(int,input().split()) #map으로 묶어서 한번에 정수형으로 처리한다.
data = list(map(int,input().split()))  #list에 입력값을 넣는다.

data.sort() #data 리스트에 입력된 숫자를 오름차순으로 정렬한다.
first = data[n-1]  #가장 큰 수 
second = data[n-2]  #두번째로 큰 수 

result =0  #결과값 저장 변수
 
while True:
    for i in range(k):  # 가장 큰 수를 k만큼 더하기 #k번 반복하는 반복문
        if m==0:
            break
        result = result+first
        m-=1
    if m==0:
        break
    result = result+ second
    m-=1
    
