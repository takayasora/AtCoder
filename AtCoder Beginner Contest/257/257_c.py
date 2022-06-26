N = int(input())
S = str(input())
Wlist = list(map(int, input().split()))

child=S.count('0')
adult=N-S.count('0')

#print(child)
#print(adult)

max_counter=0
for i in range(min(Wlist),max(Wlist)+1):
    counter=0
    for j in range(len(Wlist)):
        if i<=Wlist[j]:
            counter+=1
    
    ans=N-abs(adult-counter)
    print(i,ans)
    
    if max_counter<ans:
        max_counter=ans

print(max_counter)
