n = input()   #문자열을 입력받는다.
result = int(0)

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        result+=1

print((result+1)//2)

