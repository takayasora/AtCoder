N = int(input())
dlist=[int(input()) for i in range(N)]
sorted_dllist=sorted(dlist)
#print(sorted_dllist)
ans=0
ans = [ans+1 if sorted_dllist[i]<sorted_dllist[i+1] else ans for i in range(len(sorted_dllist)-1)]

print(sum(ans)+1)
