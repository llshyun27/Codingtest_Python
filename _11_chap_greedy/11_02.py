#0뺴고 곱하기
n = input()
m = int(1)  #결과값 출력 위해 변수 설정
for i in range(len(n)):
    if (int(n[i])!=0):  #n이 0이 아닌 경우에만 곱하기
       m = m *int(n[i])
print(m)