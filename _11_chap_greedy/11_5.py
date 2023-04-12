n,m = map(int,input().split())
weight = list(map(int,input().split()))

count = int(0)
for i in range(n-1,1,-1):
    count+=i
count =count+1

weight.sort()

same = int(0)
for j in range(n-1):
    if weight[j] ==weight[j+1]:
        same+=1
print(count - same)
