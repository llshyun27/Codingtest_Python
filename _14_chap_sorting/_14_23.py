n = int(input())  #총 학생수를 입력받는다.
student =[]   #학생 정보를 저장할 리스트
for _ in range(n):
    s = input().split()
    student.append(s)  #s에 입력된 것들을 student 리스트에 넣는다
#조건대로 정렬한다.
student.sort(key =lambda x :(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
#정렬된 student 리스트를 이름만 출력한다.
for students in student:
    print(students[0])
