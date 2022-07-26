a,b,c,d=list(map(int,input().split()))

count=0
for i in range(a,b):
    for j in range(c,d):
        if i==j:
            count+=1
print(count)