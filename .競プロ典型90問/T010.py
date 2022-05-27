N=int(input())
xy = [map(int,input().split()) for i in range(N)]
C,P=[list(i) for i in zip(*xy)]

Q=int(input())
xy = [map(int,input().split()) for i in range(Q)]
L,R=[list(i) for i in zip(*xy)]

sum_classA=0
sum_classB=0
X=[0]
Y=[0]


for j in range(N):
    if(C[j]==1):
        sum_classA+=P[j]
    else:
        sum_classB+=P[j]
    X.append(sum_classA)
    Y.append(sum_classB)


for i in range(Q):
    print(str(X[R[i]]-X[L[i]-1]) + " " + str(Y[R[i]]-Y[L[i]-1]))
    
