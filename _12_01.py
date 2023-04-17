number = input()
sum1 = int(0)
sum2 = int(0)
l = len(number)//2
for i in range(l):
    sum1 +=int(number[i])
for i in range(2*l-1,l-1,-1):
    sum2+=int(number[i])

if sum1 ==sum2:
    print("LUCKY")
else:
    print("READY")
