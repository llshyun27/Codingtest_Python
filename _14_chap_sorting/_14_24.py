n = int(input()) #집의 개수
location = list(map(int, input().split()))

location.sort()

if n %2 ==0:
    print(location[n//2-1])
else:
    print(location[n//2])


