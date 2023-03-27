from collections import deque
queue = deque()

queue.append(5)  #5
queue.append(2)  #5 2
queue.append(3)  #5 2 3
queue.append(7)  #5 2 3 7 
queue.popleft()  #2 3 7
queue.append(1)  #2 3 7 1
queue.append(4)  #2 3 7 1 4
queue.popleft()  #3 7 1 4

print(queue)    #3 7 1 4
queue.reverse()
print(queue)    #4 1 7 3