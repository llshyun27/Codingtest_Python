a,m,d,n = map(int,input().split())
count = int(0)
for i in range(n+1):
    
    count = a * m + d
    a = count 

print(count)