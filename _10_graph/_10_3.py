# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때가지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:  # b가 더 큰 경우, b의 부모를 a로 설정한다.
        parent[b] = a  # b와 a가 한팀이 된다.
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
parent = [0]*(v+1)  #부모 테이블 초기화

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges =[]
result =0

for i in range(0, v+1):
    parent[i] = i  # 부모 테이블상에서, 부모를 자기 자신으로 초기화

#모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int,input().split())
    #비용 순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost,a,b))

#간선을 비용 순으로 정렬
edges.sort()
last =0  #최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b =edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
          union_parent(parent,a,b)
          result+=cost
          last =cost

print(result-last)
