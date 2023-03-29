# S = A[0] *B[0]+....+A[N-1]*B[N-1] 
# S의 최솟값을 구한다.
# 단 B에 있는 수는 재배열 하면 안된다. 

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()  #A는 오름차순으로 정렬한다. 
s =0

for i in range(n):
    s += a[i] * max(b)  #A의 작은 수와 B의 가장 큰 수를 곱한다. 
    b.pop(b.index(max(b)))  #이미 계산된 B의 가장 큰 수는 pop으로 삭제한다. 

print(s)