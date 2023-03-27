n = int(input())
route = input().split()
x =1
y =1
nx =0
ny=0
move = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for plan in route:
    for i in range(len(move)):
        if plan ==move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx <1 or ny<1 or nx>n or ny>n:
        continue

    x,y = nx,ny

print(x, y)
            