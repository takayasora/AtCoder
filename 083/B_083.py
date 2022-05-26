N,A,B=map(int,input().split(" "))
#print(N,A,B)
ans=0
for i in range(N+1):
    sum_len=0
    for j in range(len(str(i))):
        sum_len+=int(str(i)[j])
    if(A<=sum_len<=B):
        #print(sum_len)
        ans+=i

print(ans)
