N,K = map(int,input().split())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))

sum_ans=0
for i in range(N):
    sum_ans+=abs(Alist[i]-Blist[i])

#print(sum_ans)

amari=K-sum_ans
#print(amari)

if K>=sum_ans:
    if amari%2==0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
