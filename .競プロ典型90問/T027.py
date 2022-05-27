from collections import defaultdict

d=defaultdict(bool)

N=int(input())

for i in range(N):
    s=input()
    #print(d)
    if d[s]:
        continue
    d[s]=True
    print(i+1)
