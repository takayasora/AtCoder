N=int(input())
slist=[]
for i in range(N):
    slist.append(list(input()))

flag=0
for i in range(N):
    for j in range(i,N):
        #print(slist[i][j],slist[j][i])
        if ("-"==slist[i][j]==slist[j][i]):
            continue
        if ("D"==slist[i][j]==slist[j][i]):
            continue
        if ("W"==slist[i][j] and "L"==slist[j][i]):
            continue
        if ("L"==slist[i][j] and "W"==slist[j][i]):
            continue
        flag=1
print("correct") if flag==0 else print("incorrect")