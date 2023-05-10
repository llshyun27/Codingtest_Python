n = int(input())
number = list(map(int,input().split()))
count = int(0)

for i in range(n):
    if i == number[i]:
        print(number[i])
        count +=1
if count ==0:
    print("-1")
    
#------------------------------------------------------#

def fixedpoint(number,start,end):
    if start> end:
        return None
    mid = (start+end)//2
    
    if number[mid] ==mid:   #인덱스 값과 값이 같은 경우
        return mid
    #중간 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽확인
    elif number[mid]> mid:
        return fixedpoint(number,start,mid-1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return fixedpoint(number,mid+1,end)
    
n = int(input())
number = list(map(int,input().split()))

point = fixedpoint(number,0,n-1)
if point ==None:
    print(-1)
else : 
    print(point)