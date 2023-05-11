n,m =list(map(int,input().split(' ')))
array = list(map(int,input().split()))

start =0
end = max(array)

result =0
while(start<end):
    total =0
    mid = (start + end)//2
    for x in array:
        if x>mid:
            total += total +(x-mid)
    if total<m: #자른 떡의 양이 부족한 경우
       #한칸 앞으로 잘라서 더 자르기
       end = mid -1
    else: #자른 떡의 양이 너무 많은 경우
        #한칸 뒤로 자르기
        result = mid
        start = mid+1
print(result)
