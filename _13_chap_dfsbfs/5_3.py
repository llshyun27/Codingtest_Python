n,m = map(int,input().split())   #세로 가로 입력받기

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

#dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph[x][y]==0:  # 얼음에 구멍이 뚫려있다면
        graph[x][y] =1 # 해당 구멍을 방문 한것으로 처리
        #상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        return True
    return False  #한 텀이 끝나면 False를 출력하여 다음 얼음을 구한다. 

#모든 노드에 대하여 음료수 채우기
result =0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 수행
        if dfs(i,j) ==True:
            result+=1

print(result)