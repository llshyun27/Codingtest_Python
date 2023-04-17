n, m = map(int, input().split())
weight = list(map(int, input().split()))

count = int(0)
for i in range(n):
    count += i
weight.sort()

same = int(0)
for j in range(n):
    for i in range(j,n,1):
       if weight[j] == weight[i]:
           same += 1  
same = same -n                                                                                                                                                                                                             
print(count - same)
