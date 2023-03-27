jack, daniel, andy = map(int,input().split())
d =1
while d%jack!=0 or d%daniel!=0 or d%andy:
    d+=1
print(d)