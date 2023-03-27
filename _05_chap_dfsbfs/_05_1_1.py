#스택은 박스를 쌓는 것과 같다.
#아래에서 위로 쌓기, 선입후출 방식, 후입선출 방식
stack =[]
stack.append(5)  #5
stack.append(2)  #5 2
stack.append(3)  #5 2 3
stack.append(7)  #5 2 3 7
stack.pop()      #5 2 3
stack.append(1)  #5 2 3 1
stack.append(4)  #5 2 3 1 4
stack.pop()      #5 2 3 1

print(stack)        #5 2 3 1
print(stack[::-1])  #1 3 2 5