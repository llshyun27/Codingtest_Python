#순차 탐색이란 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 
# 하나씩 차례대로 확인하는 방법이다.

def sequential_search(n,target,array):
    #각 원소를 하나씩 확인한다.
    for i in range(n):
        if array[i]==target:
            return i+1

print("생성할 원소 개수를 입력한 다음 한 칸을 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])   #원소의 개수
target = input_data[1]   #찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요.구분은 띄어쓰기 한칸")
array = input().split()

print(sequential_search(n,target,array))