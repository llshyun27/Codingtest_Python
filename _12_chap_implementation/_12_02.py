import re
s = input()
value = int(0)
numbers = re.sub(r'[^0-9]','',s)  #숫자만 추출
alpha = [i for i in s if i.isalpha()]
alpha = ''.join(alpha)
alphabet =sorted(alpha)
for i in range(len(alpha)):
      print(alphabet[i],end="")

for i in numbers:
    value+= int(i)

print(value)