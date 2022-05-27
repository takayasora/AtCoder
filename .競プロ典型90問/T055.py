N,P,Q=map(int,input().split())
Alist=list(map(int,input().split()))
sum_ans=1

for i in range(4,N):
    for j in range(3,i):
        for k in range(2,j):
            for l in range(1,k):
                for n in range(0,l):
                    if(i*j*k*l*n%P==Q):
                        sum_ans+=1
