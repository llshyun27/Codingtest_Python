#greedy는 현재 상황에서 지금 당장 좋은 것만 고르는 방법이다.

#500,100,50,10원짜리 동전들이 무수히 존재. 거슬러 줘야할 돈이 1260원일때 거슬러 줘야할 동전의 최소 개수를 구하라
n = 1260
count =0
coin_type = [500,100,50,10]
for coin in coin_type:  #리스트에 반복문을 적용한다.
    count += n //coin   # //은 나눠서 정수부분만 남기는 계산이다.
    n =n %coin   #%은 나머지를 남기는 계산이다.

print(count)