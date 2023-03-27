#bfs(큐)사용
from collections import deque
n,m = map(int,input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int,input())))

dx =[-1,1,0,0]
dy =[0,0,-1,1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y =queue.popleft()
        for i in range(4):  #현재 위치에서 네 방향으로의 위치 확인
            nx = x+dx[i]
            ny = y +dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:   #미로 찾기 공간을 벗어난 경우 무시
                continue
            if graph[nx][ny] ==0:    #벽인 경우 무시
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))