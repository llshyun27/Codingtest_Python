#선택정렬, 데이터 중 가장 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고
#그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복한다.
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):  #i =0~i = 10
    min_index =i
    for j in range(i+1,len(array)):   #두번째부터 끝까지의 값 중 가장 작은 것 고른다.
        if array[min_index]>array[j]:   
            min_index =j    #가장 작은 값(j) 골라 min_index에 넣는다. 
    array[i],array[min_index]=array[min_index],array[i]  #스와치

print(array)
