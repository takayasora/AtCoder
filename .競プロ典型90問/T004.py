H,W = map(int,input().split())
Alist = [list(map(int,input().split())) for i in range(H)]

#print(Alist)
Vsum_list=[]
Hsum_list=[]
sum_ans=0

#縦合計リストを作成
for i in range(H):
    sum_ans=0
    for j in range(W):
        sum_ans+=Alist[i][j]
    Hsum_list.append(sum_ans)
#print(Hsum_list)

#横合計リストを作成
for i in range(W):
    sum_ans=0
    for j in range(H):
        sum_ans+=Alist[j][i]
    Vsum_list.append(sum_ans)
#print(Vsum_list)

#回答リストを作成
Blist=[[0 for i in range(H)]for j in range(W)]
for i in range(H):
    for j in range(W):
        #縦合計＋横合計ー自身
        print(Hsum_list[i]+Vsum_list[j]-Alist[i][j],end="")
        
        print(" ",end="") if j!=W-1 else None
    print("")
