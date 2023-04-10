n = int(input())
coin = list(map(int,input().split()))
coin.sort() #작은 순서대로 정렬한다.
result =int(1)

for i in coin:
    if i > result: # result값이 i보다 작으면 종료 후 result 출력
        break
    else:
       result = result+i
print(result)