n = int(input())
number = input().split()
for i in range(n):
    number[i] = int(number[i])
for i in range(n-1,-1,-1):
    print(number[i],end=' ')
   
