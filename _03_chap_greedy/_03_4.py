#n이 k로 나누어 떨어질때는 n을 k로 나눈다.
#나누어 떨어지지 않을 때에는 n에서 1을 뺀다. 
#n이 1이 될 때까지 두가지의 과정을 최소 몇회 수행해야 하는지 구한다.
n,k = map(int,input().split())
count =0
while True:
   while n%k==0:
    n = n//k
    count+=1
    if n ==1:
      print(count)
      break
   while n%k !=0:
    n = n-1
    count+=1
    if n==1:
      print(count)
      break

#또 다른 풀이
#n이 k보다 크면 k로 계속 나누는 while 문을 작성한 뒤,
#나누어 떨어지지 않는다면 n-1한다.
#n이 k보다 작아지면 남은 수에 대해서 1씩 빼는 계산을 수행한다.
