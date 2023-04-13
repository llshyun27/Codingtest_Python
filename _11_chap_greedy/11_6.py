def solution(food_times,k):
       if(sum(food_times)<=k):  #리스트의 총합이 k보다 작으면 결국 음식이 없기 때문에 -1리턴
              return -1
       j= int(0)
       i = int(0)
       while True:
              if i == len(food_times):  #i값이 리스트의 길이보다 커지면 다시 1번 음식부터 먹기 시작
                  i = 0
              if food_times[i]==0:  #해당 리스트의 값이 0이면 다음 리스트에 해당하는 음식을 먹는다. 
                  i =i+1
                  continue
              elif food_times[i]!=0:  #해당 리스트의 값이 0이 아니면
                  food_times[i] = food_times[i]-1    #음식을 먹고
                  i =i+1   #다음 음식으로 이동한다.
              j = j+1
              if j == k:    # k만큼 반복하고 반복문을 중단한다. 
                    break
             
       k = i      #i는 음식이 몇번째 음식인지 알려준다.
       while True:
            if k >= len(food_times): # i값이 리스트의 길이보다 커지면 다시 1번 음식부터 먹기 시작  
               k = 0
            if food_times[k] != 0:   #k번째 음식이 0이 아닌 경우 
                   print("result = ",k+1) #k번째 음식부터 먹어야 한다고 출력한다. 
                   break
            elif food_times[k] == 0:  #k번째 음식이 0인 경우 
                   k = k+1      #그 다음으로 이동한다. 
                   continue

              
                  
solution([3,1,2],5)   #함수 호출
