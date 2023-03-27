n = int(input())
i = int(1)
result = int(0)
while True:
    result = result+i
    i = i+1
    if n<=result:
        print(result)
        break
