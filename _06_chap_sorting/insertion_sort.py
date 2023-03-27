#삽입정렬은 데이터를 하나씩 확인하며 각데이터를 적절한 위치에 삽입하는 정렬이다.
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] <array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]  # 앞에 있는 수와 비교하며 한칸씩 앞으로 당긴다.
        else:
            break

print(array)