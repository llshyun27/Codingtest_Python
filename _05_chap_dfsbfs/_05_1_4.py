#dfs(재귀함수)사용
n,m= map(int,input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m: #주어진 범위를 벗어나는 경우에는 즉시 종료
        return False
    if graph[x][y] == 0:  # 만약 현재 노드를 아직 방문하지 않았다면
        graph[x][y] =1    # 해당 노드 방문 처리

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result =0
for i in range(n):
    for j in range(m):
        if dfs(i,j) ==True:
            result+=1

print(result)