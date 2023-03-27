#19x19바둑판을 만들고 입력된 칸에 해당하는 곳을 1로 바꾼다. 
d=[]
for i in range(20):   #19x19 바둑판 만들기
    d.append([])
    for j in range(20):
        d[i].append(0)  #모든 칸을 0으로 채움

n = int(input())   #몇칸을 1로 바꿀지 입력받는다. 
for i in range(n):
    x,y = input().split()   # 1로바꿀 x,y를 n개만큼 입력받는다. 
    d[int(x)][int(y)]=1

for i in range(1,20):   #바둑판을 출력한다. 
    for j in range(1,20):
        print(d[i][j],end='')
    print()